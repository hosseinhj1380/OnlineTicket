# from dependencies import get_db

from databases import client

from pymongo import MongoClient
# db : MongoClient = Depends(get_db)
from databases import movie_collection_info



class CRUDmovies:


    def create_movie(movie_info):
        
        movie_collection_info.insert_one(movie_info)

        client.close()
        



        

