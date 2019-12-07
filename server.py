import jwt
import json
import requests
from flask import Flask, request
app = Flask(__name__)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import pyodbc
#from connecter import DBDriver

# Add server name from SQL server to access database
database_name = "DESKTOP-DAVID"

# Check if nonce was used before
# return true if valid/unused
def verify_nonce(nonce):

    con =     conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server="+database_name+";"
        "Database=master;"
        "Trusted_Connection=yes;")
    dao = DBDriver()

    nonce = 31479440252208841774839265268216512915557365329506229865177313174700711327471555987666273602936135314059536762167237420357076140127062440523094621113425221506918606512561225397049756078703714092151654862834119264754407243932068318076316558889948166196202336052688560824491435102909923683149169431394013673132449598586034560581734713680647191974086781889023951666869281734711917256667854593286402950407616984798710825224750159021665279397297950386181792534393372672433787702672759777913724164653861148

    return dao.Read_nonce(con, nonce)

    # if nonce in valid_nonces:
    #     return False
    # else:
    #     return True

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

@app.route('/server/identify')
def identify():
    
    # receive key from client
    data = requests.json
    print("JWT: "+ data)

    encrypted_message = data

    # Decode message with Private key
    message = jwt.decode(encrypted_message, private_key, algorithms=['HS256'])

    # return message encrypted with public key
    return_message = jwt.encode(message, public_key, algorithms=['HS256'])


# Key route
@app.route('/server/secure')
def process_request():

    data = requests.json

    if authenticate_client(data) == True:
        return "here is data"
    else:
        return "you are not authorized"

    headers = request.headers
    decodedJwt = jwt.decode(headers.get('Auth'), 'secret', algorithms=['HS256'])
	 	
    if decodedJwt['TestSecret'] == 'TestPassword':
        return 'Authorized, here is your data!'
    else:
        return 'Unauthorized, who do you know here?' 

def encryptMessage(pk):
    key = RSA.import_key(pk)

    encryptor = PKCS1_OAEP.new(key)
    encrypted = encryptor.encrypt(b'aliens exist')
    
    return encrypted

# take jwt
@app.route('/server/authenticate', methods=['GET','POST'])
def accept_client_jwt():
    client_jwt = request.data.decode('utf-8')

    # make sure a valid jwt is received
    try:  
        decodedJwt = jwt.decode(client_jwt, 'secret', audience='server', issuer='issuer', algorithms=['HS256'])                    
    except Exception as inst:
        print('Unexpected error: ', sys.exc_info()[0])
        exit()
    
    # Verify Nonce not used
    if verify_nonce(decodedJwt['nonce']) == False:
        print("nonce already used: possible replay attack")
        exit()
    else:
        print("nonce is unique")

    print(decodedJwt)
    # return the jwt from issuer
    encryptedMessage = encryptMessage(decodedJwt['cnf']['jwk'])
    print('Public key obtained from client!')
    return encryptedMessage

@app.route('/server/verified', methods=['GET','POST'])
def grant_access():
    creds = json.loads(request.data.decode('utf-8'))
    print(str(creds))
    con =     conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server="+database_name+";"
        "Database=master;"
        "Trusted_Connection=yes;")
    dao = DBDriver()
    cursor = conn.cursor()
    return dao.getNumber(conn, creds['first'], creds['last'])

class DBDriver:
    # change server and database per user, also change subsequent names in functions
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server="+database_name+";"
        "Database=master;"
        "Trusted_Connection=yes;")

    # Create
    def Add(value): 
        cursor.execute("INSERT INTO master.dbo.PersonalInformation (ID, Name) VALUES (?, ?);", '3', 'test')
        print(cursor.rowcount, "added value!")
        conn.commit()

    # parameterized request 
    def getNumber(self, conn, first, last):
        query = '''SELECT [PhoneNumber]
  FROM [master].[dbo].[PersonalInformation]
  WHERE  [FirstName] = 'first' AND [LastName] = 'last' '''
        query = query.replace('first', first)
        query = query.replace('last', last)
        print(query)
        cursor = conn.cursor()
        cursor.execute(query)
        ssn = ''.join(cursor.fetchone())
        conn.close
        return ssn

    # Read
    def Read(self, conn):
        print("Read")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM master.dbo.PersonalInformation;")
        for row in cursor:
            print(row)
        print()
        conn.close()

    def Read_nonce(self, conn, nonce):
        print("Reading nonce")
        print("searching for nonce: " +str(nonce))

        nonce = str(nonce).replace("'","''")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM master.dbo.LoginInfo WHERE UserKey='"+nonce+"';")
        for row in cursor:
            if len(row) > 0:
                conn.close()
                return False
        conn.close()
        return True


    # Update
    def Update(args):
        cursor.execute('UPDATE master.dbo.PersonalInformation SET column1 = newvalue, column2 = newvalue WHERE ID = 1;')
        print(cursor.rowcount, "updated!")
        conn.commit()
    # Delete
    def Delete(args):
        cursor.execute('DELETE FROM master.dbo.PersonalInformation WHERE ID = 1;')
        print(cursor.rowcount, "deleted!")
        conn.commit
        
if __name__ == '__main__':

    app.run()