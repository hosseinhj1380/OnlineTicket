
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
    
    def update_genres(self,genres_new_name,genres_name):


        if self.check_genres_availability(genre_name=genres_name):

            try:


                movies_genres_collection.update_one({"name":genres_name},
                                                   {"$set": {"name": genres_new_name}})
                return "Successfully Updated "

            except:
                return "Failed to update genres"
            
        else:
            return "Genres_name doesnt exist "
        
    def delete_genres(self,genres_name):
        if self.check_genres_availability(genre_name=genres_name):
            movies_genres_collection.delete_one({"name":genres_name})
            return "successfully deleted"
        else:
            return "genres doesnt exist "

def check_genres(genres):
    if movies_genres_collection.find_one(genres):
        return True
    else:
        return False  