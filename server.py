from flask import Flask
import jwt
app = Flask(__name__)

# test route
@app.route('/')
def hello_world():
    return 'here is your data'

def authenticate_client_key():

    # Receive key from MS ADAL
    key = ""

    # Decode key once received from AD 
    jwt.decode(key, 'secret', algorithms=['HS256'])

    # return credentials
    return True

@app.route('/generate_key_pairs')
def generate_key_pairs():
    print("calling issuer for key pairs")

    # Call issuer


# Key route
@app.route('/secure')
def process_request():
    return "here is data"


if __name__ == '__main__':
    app.run()