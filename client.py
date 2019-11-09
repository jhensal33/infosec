# jeff
# importing the requests library 
import requests 
import jwt
import json

def createJwt():
	encodedJwt = jwt.encode({'TestSecret': 'TestPassword'}, 'secret', algorithm='HS256')
	return encodedJwt 

public_key = ''
private_key = ''

def get_credentials(file_name):
    cred_file = open(file_name)
    credentials = json.load(cred_file)

    public_key = credentials['public_key']
    private_key = credentials['private_key']


def authenticate_key():

    # Receive JWT from server
    public_key = ""

    # encode message with public key 
    message = "random"
    encoded_message = jwt.encode(message, public_key, algorithms=['HS256'])
    
    # send encoded message to server
    print(encoded_message)

    # Decode key once received from AD 
    decoded_message = jwt.decode(public_key, 'secret', algorithms=['HS256'])

    # message should be equivalent
    return message == decoded_message

def sendRequest(encodedJwt):
	# sending get request and saving the response as response object 
	r = requests.get(url = URL,  headers={'Auth': encodedJwt})
	
	if r == 200:
		print('Success!')
	elif r == 404:
		print('Not Found.')

	# printing the output 
	print("Response: %s"%r.text)

if __name__ == '__main__':

    get_credentials('client_cred.json')
 
    if authenticate_key() == True:
        print("server authenticated")
    else:
        print("server is adversary")


    # sending get request and saving the response as response object 
    r = requests.get(url = URL)

    if r == 200:
        print('Success!')
    elif r == 404:
        print('Not Found.')

    # printing the output 
    print("Response: %s"%r.text)

	# local api-endpoint 
	URL = "http://127.0.0.1:5000/"
	
	sendRequest(createJwt())
	



if __name__ == '__main__':
	

	
