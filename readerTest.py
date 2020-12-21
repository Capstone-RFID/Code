from sllurp import llrp
from twisted.internet import reactor
import pyodbc
from datetime import datetime
from datetime import date
import subprocess
import keyboard

import logging
equipmentID = []

# define the server name and the database name
server = "BALKARAN09"
database = 'TEST'

# define a connection string
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                        SERVER=' + server + ';\
                          DATABASE=' + database + ';\
                        Trusted_Connection=yes;')

# create the connection cursor
cursor = cnxn.cursor()

def filterInfo(tagID):
    check = any(str(tagID[20:26]) in sublist for sublist in equipmentID) #checnk if the same equipment is already in database
    if check == False:
        print("Please Enter your Employee ID : ")
        EmployeeID = str(input())
        equipmentID.append([EmployeeID,str(tagID[20:26]),date.today().strftime("%d/%m/%Y"),datetime.now().strftime("%H:%M:%S")])
        insert()
        snapshot()

def insert():

    # define our insert and update query
    insert_query = '''INSERT INTO RFID_database(EMPLOYEE_ID,EQUIPMENT_ID,DATE,TIME) 
                        VALUES (?,?,?,?);'''  # '?' is a placeholder

    # loop thru each row in the matrix
    for row in equipmentID:
        # define the values to insert
        values = (row[0], row[1],row[2],row[3])
        print(values)
        # insert the data into the database
        cursor.execute(insert_query, values)

    # commit the inserts
    cnxn.commit()

    # grab all the rows in our database table
    #cursor.execute('SELECT * FROM Employees')

   # loop through the results
   # for row in cursor:
      #  print(row)

    # close the connection and remove the cursor
    cursor.close
    cnxn.close

##work in progress
def update():
    update_query = '''
                    UPDATE TestDB.dbo.Person
                    SET Age = 29,City = 'Montreal'
                    WHERE Name = 'Jon'
                    '''
    # loop thru each row in the matrix
    for row in equipmentID:
        # define the values to insert
        values = (row[0], row[1],row[2],row[3])
        print(values)
        # insert the data into the database
        cursor.execute(update_query, values)


def snapshot():
    subprocess.run(
        ["C:\\Program Files\\Microsoft SQL Server\\150\\COM\\snapshot.exe",
         "-Publisher", "[BALKARAN09]", "-PublisherDB", "[TEST]",
         "-Distributor", "[BALKARAN09]", "-Publication", "[please_merge]",
         "-ReplicationType", "2", "-DistributorSecurityMode", "1"],
        # probably add this
        check=True)

logging.getLogger().setLevel(logging.INFO)

def cb (tagReport):
    if  keyboard.is_pressed('q'):
        reactor.stop()
        mode = 'q'
    tags = tagReport.msgdict['RO_ACCESS_REPORT']['TagReportData']

    if len(tags) != 0:
        filterInfo(tags[0]['EPC-96'])

              
def shutdown(factory):
    return factory.politeShutdown()

factory = llrp.LLRPClientFactory(antennas=[1],start_inventory = True ,session =0,duration =0.8)
factory.addTagReportCallback(cb)
reactor.connectTCP('169.254.10.1', llrp.LLRP_PORT, factory)


def start():
    reactor.run()

def stop():
    reactor.stop()








# llrp.LLRPClientFactory(tag_content_selector={
#     'EnableROSpecID': False,
#     'EnableSpecIndex': False,
#     'EnableInventoryParameterSpecID': False,
#     'EnableAntennaID': True,
#     'EnableChannelIndex': False,
#     'EnablePeakRSSI': True,
#     'EnableFirstSeenTimestamp': False,
#     'EnableLastSeenTimestamp': True,
#     'EnableTagSeenCount': True,
#     'EnableAccessSpecID': False,
# }, ...)