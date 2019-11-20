import requests 
import jwt
import json
import os
from Crypto.PublicKey import RSA

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
# TODO: return JWT
def sendPopPublicKey(pk):

    #generate key and send to issuer
    jsonKey = '{"key":"' + str(pk) + '"}'

    print("JSON KEY TO SEND: "+ str(jsonKey))
    
    r = requests.post(url = URL, data = jsonKey)

    if r.status_code == 200:
        print('Request Successfully Received!')
        print(r.content.decode('utf-8'))
        if is_json(r.content.decode('utf-8')):
                jsload = json.loads(r.content.decode('utf-8'))
                decodedJwt = jwt.decode(jsload['jwt'], 'secret', algorithms=['HS256'])
                if decodedJwt['key'] == 'abckey1':
                    print('JWT successfully received from Issuer') 
        else:
            print("Content received isnt JSON")
            return
    elif r.status_code > 300 and r.status_code < 500:
        print('Error in Request')
    else:
        print('Error in Server' + str(r.status_code))

if __name__ == '__main__': 

	# local api-endpoint
    URL = "http://127.0.0.1:5000/"

    print("Starting Client....")

    # ============= Key creation ===============
    key = ""
    # if (input("Generate key pair?(y/n)").lower == "y"):
    key = create_credentials("credentials.txt")
    print("key written to credentials.txt")
    # else:
    #     key = load_credentials(input("input file path to credentials:"))


    # ============ send key to issuer =================

    print("sending key to issuer")
    # should return a jwt
    

    # =========== get nonce for JWT ===================
    nonce_r = generate_nonce()
    
    # =========== Send JWT to server =================
    # sending get request and saving the response as response object 

    sendPopPublicKey(key.export_key('PEM').decode("utf-8"))

