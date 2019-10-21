import jwt
import json
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
	headers = request.headers
	decodedJwt = jwt.decode(headers.get('Auth'), 'secret', algorithms=['HS256'])
	 	
	if decodedJwt['TestSecret'] == 'TestPassword':
		return 'Authorized, here is your data!'
	else:
		return 'Unauthorized, who do you know here?' 
	
		
if __name__ == '__main__':
    app.run()