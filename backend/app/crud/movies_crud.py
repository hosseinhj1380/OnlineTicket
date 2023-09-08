# from dependencies import get_db

from databases import client

from pymongo import MongoClient
# db : MongoClient = Depends(get_db)
from databases import movie_collection_info


class CRUDmovies:

    def create_movie(movie_info):

        last_document = movie_collection_info.find_one(sort=[('_id', -1)])
        if last_document:
            movie_id = last_document["movie_id"]+1
        else:
            movie_id = 1

        movie_rate = {"movie_rate": 0,
                      "rates_count": 0
                      }

        movie_collection_info.insert_one({"movie_id": movie_id,
                                          "movie_info": movie_info,
                                          "movie_rate": movie_rate,
                                          "has_been_sold": 0})

    def movie_details(movie_id):

        movie_detail = movie_collection_info.find_one(
            {"movie_id": movie_id}, {'_id': False})

        return movie_detail

    def movie_update(movie_id, movie_info):

        if movie_collection_info.find_one({"movie_id": movie_id}, {'_id': False}):
            try:
                movie_collection_info.update_one(
                    {"movie_id": movie_id},
                    {"$set": {"movie_info": movie_info}})

                return "success"
            except:

                return "failed"
        else:
            return "movie_id doesnt exist "

    def delete_movie(movie_id):
        filter = {"movie_id": movie_id}
        if movie_collection_info.find_one(filter, {'_id': False}):
            movie_collection_info.delete_one(filter)
            return "successfully deleted"
        else:
            return "movieid doesnt exist "
