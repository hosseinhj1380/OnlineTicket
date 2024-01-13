from elastic_connection import connection

client , index = connection()

def index_cinema_datas(**kwargs):
    
    document = {
    "name":kwargs.get("name")    ,
    "is_active":kwargs.get("is_active"),
    "id":kwargs.get("id"),
    "url":kwargs.get("url"),
    "type":"cinema"}
    response = client.index(index=index, body=document)
    return(response)    

def index_movies_data(**kwargs):

    document = {
    "name":kwargs.get("name")    ,
    "is_active":kwargs.get("is_active"),
    "id":kwargs.get("id"),
    "url":kwargs.get("url"),
    "type":"movie"}
    response = client.index(index=index, body=document)

    return response