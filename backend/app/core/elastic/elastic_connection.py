from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os 
load_dotenv()

# Password for the 'elastic' user generated by Elasticsearch
ELASTIC_PASSWORD = os.environ.get("ELASTIC_PASSWORD")

# Create the client instance
host=os.environ.get("ELASTIC_HOST")
print(host)

def connection():
    client = Elasticsearch(
    os.environ.get("ELASTIC_HOST"),
    ca_certs=os.environ.get("PATH_TO_HTTP_CA"),
    basic_auth=(os.environ.get("ELASTIC_USERNAME"), ELASTIC_PASSWORD)
)   
    return client , os.environ.get("ELASTIC_DOCUMENT")


# client=connection()