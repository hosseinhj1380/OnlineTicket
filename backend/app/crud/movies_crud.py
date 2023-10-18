
from databases import movie_collection_info
from .comment_crud import CRUDcommnet

class CRUDmovies:

    def create_movie(movie_info):

        last_document = movie_collection_info.find_one(sort=[('_id', -1)])
        if last_document:
            movie_id = last_document["movie_id"]+1
        else:
            movie_id = 1

        obj=CRUDcommnet()
        thread=obj.create()
        

         
        

        movie_rate = {"movie_rate": 0,
                      "rates_count": 0
                      }

        movie_collection_info.insert_one({"movie_id": movie_id,
                                          "movie_info": movie_info,
                                          "movie_rate": movie_rate,
                                          "thread":thread,
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
            return "movie id doesnt exist "


def check_thread(thread):
    if movie_collection_info.find_one({"thread":thread}):
        return True
    else:
        return False
        
        
