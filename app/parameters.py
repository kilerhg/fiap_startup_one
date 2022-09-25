from dotenv import load_dotenv
import os
import logging

load_dotenv()

API_NAME = os.environ['API_NAME']
API_SECRET_KEY = os.environ['API_SECRET_KEY']
DB_HOST = os.environ['DB_HOST']
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_PORT = os.environ['DB_PORT']