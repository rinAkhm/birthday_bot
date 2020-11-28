import mysql.connector
from dotenv import load_dotenv 
import os

load_dotenv()

def connection_db(db="save"):
    """ This fuction need for connect db server"""
    if db!=None:
        mydb = mysql.connector.connect(
            host=os.getenv('host'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            port=('port'),
            database=('database')
            )
        mycursor = mydb.cursor()
        return mycursor
    else:
        mydb.commit()
        return "Successful change"