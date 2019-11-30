import requests 
import jwt
import json
import os
import sys
import ast
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def load_credentials(file_name):
    cred_file = open(file_name)
    return RSA.import_key(cred_file.read())

def create_credentials(file_name):
    private_key = RSA.generate(2048)

    public_key = private_key.publickey()

    cred_file = open(file_name, 'wb')
    cred_file.write(private_key.export_key('PEM'))
    cred_file.close

    return public_key

# generates a cyrpto string of 32 bytes based on OS implementation
def generate_nonce():
    nonce = os.urandom(32)
    # add nonce to db?
    return nonce

# Sends client public key to issuer
# Returns jwt with embedded public key
def sendPubKeyToIssuer(pk):
    #generate key and send to issuer
    encoded_key = pk.export_key('PEM')
    json_key = json.dumps({'key': encoded_key.decode('utf-8')})

    print("JSON to send to issuer: " + str(json_key))
    
    #TODO: username/password authentication
    r = requests.post(url = issuerURL+'issue', data = json_key)
    print(str(json.loads(r.content.decode('utf-8'))))
    if r.status_code == 200:
        print('')
        print('Issuer Response Successfully Received!')
        print('')
        if is_json(r.content.decode('utf-8')):
                jsload = json.loads(r.content.decode('utf-8'))
                # make sure a valid jwt is returned
                try:  
                    decodedJwt = jwt.decode(jsload['PopJwt'], 'secret', audience='server', issuer='issuer', algorithms=['HS256'])                    
                except Exception as inst:
                    print('Unexpected error: ', sys.exc_info()[0])
                    exit()
                # return the jwt from issuer
                return jsload['PopJwt']
        else:
            print('Content received is not JSON')
            return 'error'
    elif r.status_code > 300 and r.status_code < 500:
        print('Error in Request')
        return 'error'
    else:
        print('Error in Server ' + str(r.status_code))
        return 'error'

def decryptMessage(encrypted):
    f = open('privatekey.txt', 'r')
    key = RSA.import_key(f.read())

    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))
    return decrypted

def sendJwtToServer(pop_jwt):
    #json_key = json.dumps({'key': pop_jwt.decode('utf-8')})
    r = requests.post(url = serverURL+'server/authenticate', data = pop_jwt)

    if r.status_code == 200:
        print('')
        print('Server Response Successfully Received!')
        print('Decrypting server message...')
        decryptedMessage = decryptMessage(r.content).decode('utf-8')
        print('Decrypted message: ' + decryptedMessage)
        return 
    elif r.status_code > 300 and r.status_code < 500:
        print('Error in Request' + str(r.status_code))
        return 'error'
    else:
        print('Error in Server ' + str(r.status_code))
        return 'error'    

if __name__ == '__main__':

    issuerURL = "http://127.0.0.1:5000/"
    serverURL = "http://127.0.0.1:5001/"

    print("Starting Client....")

    # ============= Key creation ===============
    pub_key = ""
    # if (input("Generate key pair?(y/n)").lower == "y"):
    pub_key = create_credentials("privatekey.txt")
    print("Private key written to privatekey.txt")
    print('')
    # else:
    #     key = load_credentials(input("input file path to credentials:"))

    # ============ send key to issuer =================

    #print("sending key to issuer")
    # should return a jwt
    pop_jwt = sendPubKeyToIssuer(pub_key)
  
    if pop_jwt == 'error':
        print('error encountered')
        exit()
 
    print('Decoded jwt from issuer: ' + str(jwt.decode(pop_jwt, 'secret', audience='server', issuer='issuer', algorithms=['HS256'])))

    # =========== get nonce for JWT ===================
    #nonce_r = generate_nonce()
    
    # =========== Send JWT to server =================
    sendJwtToServer(pop_jwt)    

    ''' code to test encryption/decryption from client/server
    # server must be running
    r = requests.get(url = 'http://127.0.0.1:5000/encrypt')
    print(decryptMessage(r.content))
    '''