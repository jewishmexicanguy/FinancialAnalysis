'''
<!DOCTYPE python>
This python file will have objects that carry out actions that process data for us
'''

import sqlite3 as sql
import json
import datetime

class SQL_Access:
    '''
    This object will give us access to a sqlit3 database
    '''

    DataBaseDirectory = "StockMarketAnalysis"

    def __init__(self):
        '''
        Class constructor

        Initiate a connection to our data base and save that object.
        '''
        self.conn = sql.connect(self.DataBaseDirectory)
        self.c = self.conn.cursor()

    def __del__(self):
        '''
        Class destructor

        Release data base connection here
        '''
        self.conn.close()

    def create_Tables(self):
        '''
        This method will create some tables for us when invoked
        '''

        create_stocks_command = '''CREATE TABLE Stocks(
        [Id] INTEGER PRIMARY KEY NOT NULL UNIQUE,
        [Symbol] TEXT NOT NULL,
        [UnixTimeStamp] INTEGER NOT NULL,
        [PriceUSD] REAL NOT NULL
        )'''
        
        self.conn.executescript(create_stocks_command)
        
        print ("Created Table Stocks")

    def destroy_Tables(self):
        '''
        This method will drop the tables when invoked
        '''
        
        drop_stocks_command = 'DROP TABLE Stocks'
        
        self.conn.executescript(drop_stocks_command)
        
        print ("Dropped Table Stocks")

    def print_Tables(self):
        '''
        This method will enumeate and dispaly the tables that live in our data base
        '''

        select_tables_querry = "SELECT name FROM sqlite_master WHERE type = 'table'"

        self.c.execute(select_tables_querry)

        for i in self.c.fetchall():
            print(i)

    def read_Table(self, table_name, records = None):
        '''
        This method will read and display the first n records from a table
        Parameters
            table_name : the table to read from
            records : how many records to return, leaving blank will return all records
        '''

        select_querry = None

        if records == None:
            select_querry = "SELECT * FROM " + table_name
        else:
            select_querry = "SELECT TOP " + records + " * FROM " + table_name

        self.c.execute(select_querry)

        for i in self.c.fetchall():
            print(i)

    def insert_Stock(self, Symbol, UNIXTimeStamp, PriceUSD):
        '''
        This is a concrete method for inserting a recortd into our table Stocks
        '''

        Data = [Symbol, UNIXTimeStamp, PriceUSD]

        self.c.execute("INSERT INTO Stocks([Symbol], [UnixTimeStamp], [PriceUSD]) VALUES(?, ?, ?)", Data)