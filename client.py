import requests 
import jwt
import json
import os
import sys
import ast
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import hashlib

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def load_credentials(file_name):
    try:
        cred_file = open(file_name)
        return RSA.import_key(cred_file.read())
    except:
        print("failed to find "+ str(file_name)+ "generating new cred file")
        return create_credentials(file_name)


def create_credentials(file_name):
    try:
        print('Generating Key Pair...')
        private_key = RSA.generate(2048)

        public_key = private_key.publickey()

        cred_file = open(file_name, 'wb')
        cred_file.write(private_key.export_key('PEM'))
        cred_file.close
    except:
        print("Failed to generate credentials")
        exit()

    return public_key
  

# generates a cyrpto string of 32 bytes based on OS implementation
def generate_nonce():
    print("generating nonce for JWT")
    nonce = os.urandom(32)
    return nonce

# Sends client public key to issuer
# Returns jwt with embedded public key
def sendPubKeyToIssuer(pk, u, p):
    #generate key and send to issuer
    encoded_key = pk.export_key('PEM')
    json_key = json.dumps({'key': encoded_key.decode('utf-8'), 'username':u, 'password':p})

    # print("JSON to send to issuer: " + str(json_key))
    
    #TODO: username/password authentication
    r = requests.post(url = issuerURL+'issue', data = json_key)
    # print(str(json.loads(r.content.decode('utf-8'))))
    if r.status_code == 200:
        print('Issuer response received')
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
            print('Issuer response is not JSON')
            print('Response from issuer: ' + str(r.content.decode('utf-8')))
            return 'error'
    elif r.status_code > 300 and r.status_code < 500:
        print('Error in Request')
        return 'error'
    else:
        print('Error in Issuer ' + str(r.status_code))
        return 'error'

def decryptMessage(encrypted):
    try:
        f = open('privatekey.txt', 'r')
        key = RSA.import_key(f.read())
    except:
        print("failed to open key file")
        exit()
    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))
    return decrypted

def sendJwtToServer(pop_jwt):
    #json_key = json.dumps({'key': pop_jwt.decode('utf-8')})
    r = requests.post(url = serverURL+'server/authenticate', data = pop_jwt)

    if r.status_code == 200:
        print('Server response received!')
        decryptedMessage = decryptMessage(r.content).decode('utf-8')
        print('Decrypted server challenge: ' + decryptedMessage)

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

    print('Enter client username for issuer:')
    u = input()
    print('Enter client password for issuer:')
    p = input()

    hashed = hashlib.sha256()
    hashed.update(p.encode('utf-8'))
    p = str(hashed.hexdigest())

    # ============= Key creation ===============
    pub_key = ""
    if (input("Generate new key pair?(y/n)") == "y"):
        pub_key = create_credentials("privatekey.txt")
        print("Private key written to privatekey.txt\n")
        
    else:
        pub_key = load_credentials(input("Input file path to credentials:"))

    # ============ send key to issuer =================

    print("Sending key to issuer")
    # should return a jwt
    pop_jwt = sendPubKeyToIssuer(pub_key, u, p)
  
    if pop_jwt == 'error':
        print('Error encountered: Exiting...')
        exit()
 
    # print('Decoded jwt from issuer: ' + str(jwt.decode(pop_jwt, 'secret', audience='server', issuer='issuer', algorithms=['HS256'])))


    # =========== Send JWT to server =================
    print('Sending Jwt to Server')
    sendJwtToServer(pop_jwt)    


    # =========== Once verified send commands ===========
    print('')
    print('You are verified and may now send requests to protected resource.\n')
    print('Enter the the first and last name of the person whose social security number you need.')
    print('Type \'EXIT\' to exit the program.')
    action = ''
    while(action != "EXIT" and action != "exit"):

        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        action_nonce = generate_nonce()
        creds = json.dumps({'first':first_name, 'last':last_name, 'nonce':str(action_nonce)})

        r = requests.post(url = serverURL+'server/verified', data = creds)        
        print("Social Security Number: " + r.content.decode('utf-8'))

        action = input("Enter any key to continue or \'EXIT\' to exit: ")
 
    # Exit program
    print("Exiting client application")