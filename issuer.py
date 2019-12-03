import jwt
import json
from flask import Flask, request, Response
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import ast

app = Flask(__name__)

def createJwt(publicKey):
    print('Creating Jwt')
    #TODO: generate key and signature protect jwt?
    encodedJwt = jwt.encode({'cnf': {'jwk':str(publicKey)}, 'aud':'server', 'iss':'issuer'}, 'secret', algorithm='HS256')
    print('Jwt Created')
    return encodedJwt

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

@app.route('/issue', methods=['GET','POST'])
def issueJwt():

    if is_json(request.data):
        print("Client request is json!")
        json_key = json.loads(request.data)
        jwtWithKey = createJwt(json_key['key'])

        js = json.loads('{"PopJwt":"here"}')
        js['PopJwt'] = jwtWithKey.decode('utf-8')
    
        return js
    else:
        return "FAIL"

if __name__ == '__main__':
    app.run()
