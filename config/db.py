import os
from dotenv import load_dotenv

load_dotenv()
# Database configuration
SQLALCHEMY_DATABASE_URI= os.getenv('DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
