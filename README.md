# Proof of Possession Project
**PREREQUISITES:** 
Python 3.7+

## Setting up the server
1. Open terminal (cmd for Windows or bash for macOS) and navigate to desired root directory
2. **If you haven't ever run the server before,** from desired root directory, create virtual environment by running the command below. 
```python
py -m venv env 
```
```
env\Scripts\activate 
```

3. Install Dependencies
```python
pip install flask 
pip install pyJWT
pip install requests
pip install pycryptodome
```
4. Set environment variable for the FLASK_APP to be the flask server we made:
```python
set FLASK_APP=server.py
```
or for macOS
```python
export FLASK_APP=server.py (mac)
```
5. Now, setup is done. Run the server by executing the command below. Make sure server.py is in your root directroy
```
flask run --port 5001
```

## Setting Up the Issuer
1. Open a new terminal window and create a new virtual environment
```python
py -m venv env
```
```
env\Scripts\activate 
```
2. Install Dependencies
```python
pip install flask 
pip install pyJWT
pip install requests
pip install pycryptodome
```
3. Set environment variable for the FLASK_APP to be the flask server we made:
```python
set FLASK_APP=issuer.py
```
or for macOS
```python
export FLASK_APP=issuer.py (mac)
```

4. Now, setup is done. Run the server by executing the command below. Make sure issuer.py is in your root directroy
```
flask run --port 5000
```

## Setting Up the Client
**PREREQUISITES:** Make sure the client is running (get to step 5 above)
1. Open a new terminal window and create a new virtual environment(you should have a total of 3 windows now)
2. Activate the same virtual environment by running the command from step 3 above.
```python
py -m venv env
```
```
env\Scripts\activate 
```
2. Install Dependencies
```python
pip install flask 
pip install pyJWT
pip install requests
pip install pycryptodome
```
4. Now simply run the client program by executing command below. Make sure you have the client.py in the root directory. You should see "Response: here is your data" if successful
```python
py client.py
```
5. Deactivate the virtual environment by running the same command as in step 6 above.

Bam! You made connection to the server from the client. You can also test this in your browser by typing the url listed after running the server (should be "http://127.0.0.1:5001/" and you will see the response)

## Setting up the Middleware to SQL Server
**Assuming the Server is all set up and pyodbc isn't installed**install pyodbc to this environment by running the command below.
```python
pip install pyodbc
```
1. Open up Sql Server Management Studio and connect to your server
2. Find the server name (ex. RON\SQLEXPRESS)
3. Find the database name (ex. TestDB)
4. Get table name (ex. dbo.Person)
5. TODO (enter the asked information once server.py is activated)

