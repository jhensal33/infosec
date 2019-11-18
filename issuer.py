import jwt
import json
from flask import Flask, request, Response

app = Flask(__name__)

def createJwt(publicKey):
    print('entering createjwt...')
    encodedJwt = jwt.encode(publicKey, 'secret', algorithm='HS256')
    return encodedJwt

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

@app.route('/', methods=['GET','POST'])
def issueJwt():

    if is_json(request.data):
        print("request is json!")
        jsonKey = json.loads(request.data)
        jwtWithKey = createJwt(jsonKey)

    js = json.loads('{"jwt":"here"}')
    js['jwt'] = jwtWithKey.decode('utf-8')
    
    return js

if __name__ == '__main__':
    app.run()
