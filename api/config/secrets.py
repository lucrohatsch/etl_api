import os
from dotenv import load_dotenv

load_dotenv('../.env')

ELASTIC_URL = os.environ.get("ELASTIC_URL")
ELASTIC_USR = os.environ.get("ELASTIC_USR")
ELASTIC_PSW = os.environ.get("ELASTIC_PSW")
