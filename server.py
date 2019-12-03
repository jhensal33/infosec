import jwt
import json
import requests
from flask import Flask, request
app = Flask(__name__)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Check if nonce was used before
# return true if valid/unused
def verify_nonce(nonce):
    return True

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

# Ensure that client is trusted
# break JWT into components to check
def authenticate_client(message):

    # Decode key once received from AD 
    jwt.decode(message, private_key, algorithms=['HS256']) 
    
    if verify_nonce("") == False:
        print("nonce already used: possible replay attack")
        return False
    else:
        return True

@app.route('/server/identify')
def identify():
    
    # receive key from client
    data = requests.json
    print("JWT: "+ data)

    encrypted_message = data

    # Decode message with Private key
    message = jwt.decode(encrypted_message, private_key, algorithms=['HS256'])

    # return message encrypted with public key
    return_message = jwt.encode(message, public_key, algorithms=['HS256'])


# Key route
@app.route('/server/secure')
def process_request():

    data = requests.json

    if authenticate_client(data) == True:
        return "here is data"
    else:
        return "you are not authorized"

    headers = request.headers
    decodedJwt = jwt.decode(headers.get('Auth'), 'secret', algorithms=['HS256'])
	 	
    if decodedJwt['TestSecret'] == 'TestPassword':
        return 'Authorized, here is your data!'
    else:
        return 'Unauthorized, who do you know here?' 

def encryptMessage(pk):
    key = RSA.import_key(pk)

    encryptor = PKCS1_OAEP.new(key)
    encrypted = encryptor.encrypt(b'aliens exist')
    
    return encrypted

# take jwt
@app.route('/server/authenticate', methods=['GET','POST'])
def accept_client_jwt():
    client_jwt = request.data.decode('utf-8')
    # make sure a valid jwt is received
    try:  
        decodedJwt = jwt.decode(client_jwt, 'secret', audience='server', issuer='issuer', algorithms=['HS256'])                    
    except Exception as inst:
        print('Unexpected error: ', sys.exc_info()[0])
        exit()
    
    print(decodedJwt)
    # return the jwt from issuer
    encryptedMessage = encryptMessage(decodedJwt['cnf']['jwk'])
    print('Public key obtained from client!')
    return encryptedMessage

if __name__ == '__main__':

    app.run()