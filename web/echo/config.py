import os


SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "changeme"
DEBUG = os.environ.get('DEBUG', False)
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_SERVICE = "postgres"
DB_PORT = "5432"
SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
)
