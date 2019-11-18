import requests 
import jwt 
import json

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def generateKeys():
    #TODO generate asymmetric key pair
    #TODO send public key in json format
    return '{"key":"abckey1"}'

def sendPopPublicKey():

    #generate key and send to issuer
    jsonKey = generateKeys()
    r = requests.post(url = URL, data = jsonKey)

    if r.status_code == 200:
        print('Request Successfully Received!')
        print(r.content.decode('utf-8'))
        if is_json(r.content.decode('utf-8')):
                jsload = json.loads(r.content.decode('utf-8'))
                decodedJwt = jwt.decode(jsload['jwt'], 'secret', algorithms=['HS256'])
                if decodedJwt['key'] == 'abckey1':
                    print('JWT successfully received from Issuer') 
    elif r.status_code > 300 and r.status_code < 500:
        print('Error in Request')
    else:
        print('Error in Server')

if __name__ == '__main__':
	
    # local api-endpoint 
    URL = "http://127.0.0.1:5000/"

    sendPopPublicKey()
    	
	
