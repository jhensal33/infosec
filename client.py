# importing the requests library 
import requests 
import jwt

# api-endpoint 
URL = "http://127.0.0.1:5000/"


def authenticate_key():

    # Receive JWT from server
    public_key = ""

    # encode message with public key 
    message = "random"
    encoded_message = jwt.encode(message, public_key, algorithms=['HS256'])
    
    # send encoded message to server
    print(encoded_message)

    # Decode key once received from AD 
    decoded_message = jwt.decode(public_key, 'secret', algorithms=['HS256'])

    # message should be equivalent
    return message == decoded_message



if __name__ == '__main__':

    if authenticate_key() == True:
        print("server authenticated")
    else:
        print("server is adversary")


    # sending get request and saving the response as response object 
    r = requests.get(url = URL)

    if r == 200:
        print('Success!')
    elif r == 404:
        print('Not Found.')

    # printing the output 
    print("Response: %s"%r.text)
