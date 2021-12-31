import os

from dotenv import load_dotenv
load_dotenv()

db_user = os.getenv('db_Username')
db_password = os.getenv('db_password')
