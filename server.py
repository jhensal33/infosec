import jwt
import json
import requests
from flask import Flask, request
app = Flask(__name__)

public_key = ''
private_key = ''

def get_credentials(file_name):
    cred_file = open(file_name)
    credentials = json.load(cred_file)

    public_key = credentials['public_key']
    private_key = credentials['private_key']

# Ensure that client is trusted
def authenticate_client(message):

    # Decode key once received from AD 
    jwt.decode(message, private_key, algorithms=['HS256'])

    # return credentials
    return True


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

    get_credentials('server_cred.json')

    app.run()