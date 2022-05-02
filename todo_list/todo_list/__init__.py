from flask import Flask
import os 
from dotenv import load_dotenv 

load_dotenv()
SECRET_KEY = os.environ.get("KEY")
DB_NAME = os.environ.get("DB_NAME")
print(SECRET_KEY)


def create_app(): 
    app = Flask(__name__) 
    return app 

