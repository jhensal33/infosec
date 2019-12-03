import jwt
import json
from flask import Flask, request, Response
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import ast

app = Flask(__name__)

def createJwt(publicKey):
    print('Creating Jwt...')
    #TODO: generate key and signature protect jwt?
    encodedJwt = jwt.encode({'cnf': {'jwk':str(publicKey)}, 'aud':'server', 'iss':'issuer'}, 'secret', algorithm='HS256')
    print('Jwt Created!')
    return encodedJwt

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def authenticate(username, password):
    return username == 'infosec' and password == '1fa6c67436facbf786c4b1de65824d7dd2b1a97a45c255dce2b75bd90ada8aab'

@app.route('/issue', methods=['GET','POST'])
def issueJwt():

    if is_json(request.data):
        print("Client request received")        
        json_key = json.loads(request.data)
        if(not(authenticate(json_key['username'], json_key['password']))):
            print("Authentication error")
            return "Authentication error"
        jwtWithKey = createJwt(json_key['key'])
        js = json.loads('{"PopJwt":"here"}')
        js['PopJwt'] = jwtWithKey.decode('utf-8')
    
        return js
    else:
        return "Client Request Is Not JSON"

if __name__ == '__main__':
    app.run()
