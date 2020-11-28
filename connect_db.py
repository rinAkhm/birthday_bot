import mysql.connector
from dotenv import load_dotenv 
import os

load_dotenv()

def connection_db():
    """ This fuction need for connect db server"""
    mydb = mysql.connector.connect(
            host=os.getenv('host'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            port=os.getenv('port'),
            database=os.getenv('database')
            )
    return mydb
