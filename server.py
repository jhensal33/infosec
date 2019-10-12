from flask import Flask
import jwt
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'here is your data'


def authenticate_client_key():

    # Decode key once received from AD 
    jwt.decode(key, 'secret', algorithms=['HS256'])

    # return credentials
    return ""

# Key route
@app.route('??')
    authenticate_client_key()
    return

if __name__ == '__main__':
    app.run()