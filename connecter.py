import pyodbc

# normally ask for server info but for now its default

# change server and database per user, also change subsequent names in functions
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-VQSKFMD;"
    "Database=TESTDB;"
    "Trusted_Connection=yes;")

# Create
def Add(value): 
    cursor.execute("INSERT INTO TESTDB.dbo.TestTable (ID, Name) VALUES (?, ?);", '3', 'test')
    print(cursor.rowcount, "added value!")
    conn.commit()

# Read
def Read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TESTDB.dbo.TestTable;")
    for row in cursor:
        print(row)
    print()
    conn.close()
# Update
def Update(args):
    cursor.execute('UPDATE DBName.dbo.TableName SET column1 = newvalue, column2 = newvalue WHERE ID = 1;')
    print(cursor.rowcount, "updated!")
    conn.commit()
# Delete
def Delete(args):
    cursor.execute('DELETE FROM DBName.dbo.TableName WHERE ID = 1;')
    print(cursor.rowcount, "deleted!")
    conn.commit()

# Testing - passed it outputed the data inside table.
cursor = conn.cursor()
Read(conn)