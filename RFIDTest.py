import pyodbc

for driver in pyodbc.drivers():
    print(driver)

data = [['Bal','A00826348'],
        ['abf','akhjfia']]

#define the server name and the database name

server = "BALKARAN09"
database = 'TEST'

#define a connection string
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                      SERVER=' +server+ ';\
                        DATABASE=' +database+';\
                      Trusted_Connection=yes;')

#create the connection cursor
cursor = cnxn.cursor()

#definbe our insert query

insert_query = '''INSERT INTO Employees(NAME,ID)
                    VALUES (?,?);''' #'?' is a placeholder

update_query = '''
                UPDATE TestDB.dbo.Person
                SET Age = 29,City = 'Montreal'
                WHERE Name = 'Jon'
                '''

#loop thru each row in the matrix
for row in data:
    #define the values to insert
    values = (row[0],row[1])
    print(values)
    #insert the data into the database
    cursor.execute(insert_query,values)


#commit the inserts
cnxn.commit()

#grab all the rows in our database table
cursor.execute('SELECT * FROM Employees')

#loop through the results
for row in cursor:
    print(row)

#close the connection and remove the cursor
cursor.close
cnxn.close

























