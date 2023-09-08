from databases import client

from pymongo import MongoClient
# db : MongoClient = Depends(get_db)
from databases import movies_genres_collection


class CRUDgenres:

    def __init__(self) -> None:
        pass

    def check_genres_availability(self,genre_name):

        if movies_genres_collection.find_one({"name":genre_name}):return True
        else:return False

    def create_genres(self,new_genre_name):

        if self.check_genres_availability(genre_name=new_genre_name):
            return "genres already is available"
        else:


            try:

                last_genres = movies_genres_collection.find_one(sort=[('_id', -1)])

                if last_genres:
                    genres_id = last_genres["id"]+1
                else:
                    genres_id = 1

                movies_genres_collection.insert_one({"id":genres_id,
                                                    "name":new_genre_name})
                
                return f"genres  {new_genre_name}  added successfully "
            
            except  :
                return None



    def get_genres_details(self):

        return  movies_genres_collection.find({},{"name": 1, "id": 1, "_id": 0})
        