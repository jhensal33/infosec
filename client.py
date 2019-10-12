# importing the requests library 
import requests 
import jwt

# api-endpoint 
URL = "http://127.0.0.1:5000/"


def authenticate_key():

    # Hit AD and retrieve JWT
    key = ""

    # Decode key once received from AD 
    jwt.decode(key, 'secret', algorithms=['HS256'])

    # return credentials
    return ""


if __name__ == '__main__':

    credentials = authenticate_key()

    # sending get request and saving the response as response object 
    r = requests.get(url = URL)

    if r == 200:
        print('Success!')
    elif r == 404:
        print('Not Found.')

    # printing the output 
    print("Response: %s"%r.text)
