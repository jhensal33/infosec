# jeff
# importing the requests library 
import requests 
import jwt 

def createJwt():
	encodedJwt = jwt.encode({'TestSecret': 'TestPassword'}, 'secret', algorithm='HS256')
	return encodedJwt 

def sendRequest(encodedJwt):
	# sending get request and saving the response as response object 
	r = requests.get(url = URL,  headers={'Auth': encodedJwt})
	
	if r == 200:
		print('Success!')
	elif r == 404:
		print('Not Found.')

	# printing the output 
	print("Response: %s"%r.text)

if __name__ == '__main__':
	
	# local api-endpoint 
	URL = "http://127.0.0.1:5000/"
	
	sendRequest(createJwt())
	
	