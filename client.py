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

    pubkey_file = open("pubkey.txt", 'wb')
    pubkey_file.write(public_key.export_key('PEM'))
    pubkey_file.close

    return public_key

# generates a cyrpto string of 32 bytes based on OS implementation
def generate_nonce():
    nonce = os.urandom(32)
    # add nonce to db?
    return nonce


# Sends client public key to issuer 
# TODO: return JWT
def sendPopPublicKey(pk):

    #generate key and send to issuer
    jsonKey = '{"key":"' + str(pk) + '"}'
    
    #TODO: use this, but need to encode pk somehow
    #jsonKey = json.dumps({'key': pk})

    print("JSON to send to issuer: " + str(jsonKey))
    
    r = requests.post(url = URL+'issue', data = jsonKey)

    if r.status_code == 200:
        print('Issuer Response Successfully Received!')
        if is_json(r.content.decode('utf-8')):
                jsload = json.loads(r.content.decode('utf-8'))
                # make sure a valid jwt is returned
                try:  
                    decodedJwt = jwt.decode(jsload['jwt'], 'secret', algorithms=['HS256'])                    
                except Exception as inst:
                    print('Unexpected error: ', sys.exc_info()[0])
                    exit()
                # return the jwt from issuer
                return jsload['jwt']
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

    f = open('credentials.txt', 'r')
    key = RSA.import_key(f.read())

    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))
    return decrypted

if __name__ == '__main__':

	# local api-endpoint
    URL = "http://127.0.0.1:5000/"

    print("Starting Client....")

    # ============= Key creation ===============
    pub_key = ""
    # if (input("Generate key pair?(y/n)").lower == "y"):
    pub_key = create_credentials("privatekey.txt")
    #key = key.export_key('PEM').decode("utf-8")
    #key = key.replace("\r","")
    #key = key.replace("\n","")
    print("key written to privatekey.txt")
    # else:
    #     key = load_credentials(input("input file path to credentials:"))

    # ============ send key to issuer =================

    #print("sending key to issuer")
    # should return a jwt
    popJwt = sendPopPublicKey(pub_key)
  
    if popJwt == 'error':
        print('error encountered')
        exit()
 
    print('Decoded jwt from issuer: ' + str(jwt.decode(popJwt, 'secret', algorithms=['HS256'])))

    #print(popJwt)
    
    # =========== get nonce for JWT ===================
    #nonce_r = generate_nonce()
    
    # =========== Send JWT to server =================
    # sending get request and saving the response as response object 
    

    ''' code to test encryption/decryption from client/server
    r = requests.get(url = 'http://127.0.0.1:5000/encrypt')
    print(decryptMessage(r.content))
    '''