from dotenv import load_dotenv
import os

load_dotenv()

class ProjectConfig:
    db_host = os.getenv('HOST')
    db_user = os.getenv('USER')
    db_password = os.getenv('PASSWORD')
    db_port = os.getenv('PORT')
    db_name = os.getenv('DB_NAME')
    api_host_admin = os.getenv('Host_admin')


project_config = ProjectConfig()
