import os
from dotenv import load_dotenv
load_dotenv()

TG_TOKEN = os.environ['TG_TOKEN']

db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
database = os.environ['DATABASE']
db_host = os.environ['DB_HOST']