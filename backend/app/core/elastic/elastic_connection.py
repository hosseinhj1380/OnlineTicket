# from elasticsearch import Elasticsearch
# import os 
# from dotenv import load_dotenv
# load_dotenv()


# CLOUD_ID = os.environ.get("CLOUD_ID")

# api_key = 'your-api-key'

# # Create an Elasticsearch instance with Cloud ID and API key
# es = Elasticsearch(
#     cloud_id=CLOUD_ID,
#     http_auth=(api_key, 'https://my-deployment-104f57.es.europe-west3.gcp.cloud.es.io'),
# )

# # Check if the connection is successful
# if es.ping():
#     print("Connected to Elasticsearch on Elastic Cloud")
# else:
#     print("Could not connect to Elasticsearch on Elastic Cloud")


# # {'name': 'instance-0000000000




from elasticsearch import Elasticsearch
api_key ="'


from elasticsearch import Elasticsearch
es = Elasticsearch(
    api_key="My_deployment:",
    
)
print(es.info)