from dotenv import load_dotenv
import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

if os.environ['API_MODE'] == 'development':
    logging.basicConfig(level=logging.DEBUG)