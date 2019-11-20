import jwt
import json
import requests
from flask import Flask, request
app = Flask(__name__)
from Crypto.PublicKey import RSA
    

# Check if nonce was used before
# return true if valid/unused
def verify_nonce(nonce):
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

# generates a cyrpto string of 32 bytes based on OS implementation
@app.route('/get_nonce')
def generate_nonce():
    nonce = os.urandom(32)
    # add nonce to db?
    return nonce


# test route
@app.route('/')
def hello_world():
    return 'here is your data'


@app.route('/api/identify')
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
@app.route('/api/secure')
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
	
		
if __name__ == '__main__':

    app.run()