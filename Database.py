import sqlite3
db="LoginInfo.db"; 
#Thsi file contains functions to add, search, and delete stuff from the database in python. 

#function to create a table (for our purposes, there will only ever be one table being used... ever....)
def createTable(): 
    conn=sqlite3.connect(db); 
    conn.execute("""CREATE TABLE LOGININFO
                (USERNAME TEXT NOT NULL, 
                PASSWORD TEXT NOT NULL, 
                WEBSITE TEXT NOT NULL)
    
    """)
    print("Table created successfully"); 
    conn.close(); 
#initial db stuff 

#function to add an entry to the database 
'''an entry will look like the following: Username, Password, Website '''
def addEntry(Username, Password, Website): 
    pass; 

#function to search the database by key word or phrase 
def search(phrase): 
    pass; 
#function to delete an entry by 