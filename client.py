# jeff
# importing the requests library 
import requests 
import jwt
import json
from Crypto.PublicKey import RSA

def createJwt():
	encodedJwt = jwt.encode({'TestSecret': 'TestPassword'}, 'secret', algorithm='HS256')
	return encodedJwt 

def load_credentials(file_name):
    cred_file = open(file_name)
    return RSA.import_key(cred_file.read())

def create_credentials(file_name):
    key = RSA.generate(2048)
    cred_file = open(file_name, 'wb')
    cred_file.write(key.export_key('PEM'))
    cred_file.close

    return key



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

    print("Starting Client....")

    # ============= Key creation ===============
    key = ""
    if (input("Generate key pair?(y/n)").lower == "y"):
        key = create_credentials("credentials.txt")
        print("key written to credentials.txt")
    else:
        key = load_credentials(input("input file path to credentials:"))


    # ============ send key to issuer =================
    print("sending key to issuer")
    # should return a jwt
    

    # =========== get/send nonce to JWT ===================
    nonce_r = requests(URL + "/get_nonce")
    if nonce_r == 200:
        print('Success!')
    elif nonce_r == 404:
        print('Not Found.')
        

    # =========== Send JWT to server =================
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