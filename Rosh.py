'''
<!DOCTYPE python>
This is the begining file for a  bitcoin market analysis module written in python
'''

import sqlite3 as sql
import json
import datetime

class BitcoinNetwork:
    	'''
		This object will provide access to data from the bitcoin network
		'''
	
		def foo(self):
    		print ('Test Complete')
		
class SQL_Access:
    	'''
		This class will be responsible for connecting to our Sqlite3 Data Base
		'''
	
		# declare class residents here
		DataBaseDirectory = "BitcoinFinancialAnalysis.db"
	
		def __init__(self):
    			'''
				Initiate a connection to our DataBase and store that connection object.
				'''
		
		self.conn = sql.connect(self.DataBaseDirectory)
		self.c = self.conn.cursor()
		
		def __del__(self):
    			'''
				Class destructor that will close our DataBase connection
				'''
		self.conn.close()
		
		def CreateTables(self):
    			'''
				This method will construct oour tables in our Data Base
				'''
		
				self.conn.executescript('''
				CREATE TABLE BitcoinPrice(
			    [Id] INTEGER PRIMARY KEY NOT NULL UNIQUE,
             	[tid] INTEGER NOT NULL,
			    [UnixTimeStamp] INTEGER NOT NULL,
			    [PriceUSD] REAL NOT NULL,
                [Type] INTEGER NOT NULL
				)
				''')
				print ("Created Table BitcoinPrice")
  
		def DestroyTables(self):
				'''
       			We need functionality to destroy these tables.
       			'''
      
				self.conn.executescript('''
          		DROP TABLE BitcoinPrice
				''')

				print ("Droped table BitcoinPrice")
		
		def SelectTables(self):
				'''
				We need functionality to get the tables that exist in this data base.
				'''
     
				results = self.conn.executescript('''
     			SELECT * FROM sqlite_master WHERE type = 'table'
				''')
				print('here')
				for result in results:
    					print(result)
     
		def InsertPrice(self, UnixTimeStamp, USDPrice):
				'''
				This method will insert a singular record into our bitcoin price table.
				'''
		
				Data = [UnixTimeStamp, USDPrice]
				# Perhaps we should make sure  that the record we are about to insert has a larger timestamp thane the largest timestamp in our table
				LastTime = ''
				for i in self.c.execute("SELECT MAX([UnixTimeStamp]) FROM BitcoinPrice"):
    					print (i[0])
						LastTime = i[0]
				# if the current UnixTimeStamp is larger than the largest timestamp in our table insert it.
				if LastTime < UnixTimeStamp:
						self.c.execute("INSERT INTO BitcoinPrice([UnixTimeStamp], [PriceUSD]) VALUES(?, ?)", Data)
						statement = "Inserted " + str(UnixTimeStamp) + " & " + str(USDPrice) + " into table BitcoinPrice"
						self.conn.commit()
				# otherwise inform the operator that this value was not inserted
				else:
						statement = "Value timestamp: {0}, USDPrice: {1} was not inserted into our table".format(UnixTimeStamp, USDPrice)
				# print a statement to standard output
				print (statement)
		
		def ReadTable_BitcoinPrice(self):
    			'''
				This will select all rows from the BitcoinPrice table
				'''
		
				# make a query to our DataBase
				for i in self.c.execute("SELECT [Id], [UnixTimeStamp], [PriceUSD] FROM BitcoinPrice"):
    					# print each row that was returned from our query
						print ('ID: {0}, UnixTime: {1}, USD: {2}'.format(str(i[0]), datetime.datetime.utcfromtimestamp(i[1]), str(i[2])))

class TradesParser:
    	'''
		This class will be responsible for accepting a file csv or JSON.
		Methods from another class will be responsible for inputing this into a Sqlite3 Data Base.
		'''
	
		# decalre class residents here
		active = False
	
		def __init__(self):
    			self.active = True

		def foo(self):
				print (self.active)
		
		def ParseCSV(self, CSVFile):
				# access the csv file
		
				# access/create a sqlite3 Data Base
		
				# iterate over entries in the CSV file
		
				# sqlite3 statement that inserts each row into some table/tables
			
				pass
		
		def ParseJSON(self, JSON_Object):
				'''
				This method will parse a JSON object and then insert it into our Table BitcoinPrice.
				'''
		
				workingSQL = SQL_Access()
		
		
		def Parse_JSON_File(self, file_directory):
				'''
				Open a connection to the file.
				Read in the JSON string, loop over each key pair, for each key-pair insert a record into our table.
				'''
		
				# open our json file object with read permision in python
				workingFile = open(file_directory, 'r')
				# instantiate a sql connection class object
				workingSQL = SQL_Access()
				# iterate over our json file's values
				for i in json.load(workingFile)['values']:
						# get the values from our json object by using the keys in it
						workingSQL.InsertPrice(i.get('x'), i.get('y'))
						# after finished close our file object
						workingFile.close()
		
#a = SQL_Access()
#a.CreateTables()

a = TradesParser()
a.Parse_JSON_File('chart-data.json')

a = SQL_Access()
a.ReadTable_BitcoinPrice()

a = SQL_Access()
#a.DestroyTables()
#a.CreateTables()
a.SelectTables()
