import pyodbc

# Use this class to connect and request informaiton from the database
class DatabaseConn:
    
    # Enter a string with the name of the laptop
    def __init__(self, server):
        self.conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=" + server + ";"
            "Database=master;"
            "Trusted_Connection=yes;")
        self.cursor = self.conn.cursor()


    # Create
    def Add(self, value): 
        self.cursor.execute("INSERT INTO master.dbo.TestTable (ID, Name) VALUES (?, ?);", '3', 'test')
        print(self.cursor.rowcount, "added value!")
        self.conn.commit()

    # Read, return the entire list from Personal Information
    def ReadAll(self):
        self.cursor.execute("SELECT * FROM master.dbo.PersonalInformation;")
        return self.cursor.fetchall()

    def ReadOne(self, username):
        self.cursor.execute("SELECT * FROM master.dbo.PersonalInformation WHERE username = " + username + ";")
        return self.cursor.fetchone()
        
    # Update
    def Update(self, args):
        self.cursor.execute('UPDATE master.dbo.PersonalInformation SET column1 = newvalue, column2 = newvalue WHERE ID = 1;')
        print(self.cursor.rowcount, "updated!")
        self.conn.commit()
    # Delete
    def Delete(self, args):
        self.cursor.execute('DELETE FROM master.dbo.PersonalInformation WHERE ID = 1;')
        print(self.cursor.rowcount, "deleted!")
        self.conn.commit()

# Testing - passed it outputed the data inside table.

print("runs")
test = DatabaseConn("DESKTOP-VQSKFMD")
rows = test.ReadAll()
for row in rows:
    print(row)