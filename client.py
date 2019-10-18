# jeff
# importing the requests library 
import requests 

# api-endpoint 
URL = "http://127.0.0.1:5000/"

# sending get request and saving the response as response object 
r = requests.get(url = URL)

if r == 200:
    print('Success!')
elif r == 404:
    print('Not Found.')

# printing the output 
print("Response: %s"%r.text)
