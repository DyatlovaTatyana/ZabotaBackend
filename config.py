from dotenv import load_dotenv
import os

load_dotenv()

class Adminconfig:
    host_admin = os.getenv('Host_admin') #обязательно это в класс засовывать ?
class Dbconfig:
    host = os.getenv('HOST')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    port = os.getenv('PORT')
    db_name = os.getenv('DB_NAME')