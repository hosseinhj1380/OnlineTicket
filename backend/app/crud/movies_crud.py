from databases import movie_collection_info
from .comment_crud import CRUDcommnet
from .genres_crud import check_genres
from .category_crud import check_category
from .persons_crud import check_user_ID
from datetime import datetime


class CRUDmovies:
    def __init__(self):
        pass

    def return_error(self, title, name):
        return {"status": "Error", "message": f"{title}: {name} are not available "}

    def create_thread(self):
        last_thread = movie_collection_info.find_one(sort=[("_id", -1)])

        if last_thread:
            thread = last_thread["thread"] + 1
        else:
            thread = 1

        return thread

    def create_movie(self, movie_info):
        last_document = movie_collection_info.find_one(sort=[("_id", -1)])
        if last_document:
            movie_id = last_document["movie_id"] + 1
        else:
            movie_id = 1

        thread = self.create_thread()

        movie_rate = {"movie_rate": 0, "rates_count": 0}

        for genre in movie_info["genres"]:
            if check_genres(genres=genre):
                pass
            else:
                return self.return_error(title="Genres", name=genre)

        for category in movie_info["categories"]:
            if check_category(category):
                pass
            else:
                return self.return_error(title="category", name=category)

        producers = self.check_person_ID(movie_info.get("producers"))

        if isinstance(producers, int):
            return self.return_error(title="producer", name=producers)
        else:
            movie_info["producers"] = producers

        directors = self.check_person_ID(movie_info.get("directors"))
        if isinstance(directors, int):
            return self.return_error(title="director", name=directors)
        else:
            movie_info["directors"] = directors

        actors = self.check_person_ID(movie_info.get("actors"))

        if isinstance(actors, int):
            return self.return_error(title="actors", name=actors)
        else:
            movie_info["actors"] = actors

        movie_collection_info.insert_one(
            {
                "movie_id": movie_id,
                "movie_info": movie_info,
                "created_at": str(datetime.now()),
                "movie_rate": movie_rate,
                "thread": thread,
                "has_been_sold": 0,
            }
        )
        return {"status": "Success", "message": "movie created successfully "}

    def movie_details(self, movie_id):
        movie_detail = movie_collection_info.find_one(
            {"movie_id": movie_id}, {"_id": False}
        )

        return movie_detail

    def movie_update(self, movie_id, movie_info):
        if movie_collection_info.find_one({"movie_id": movie_id}, {"_id": False}):
            try:
                movie_collection_info.update_one(
                    {"movie_id": movie_id}, {"$set": {"movie_info": movie_info}}
                )

                return "success"
            except:
                return "failed"
        else:
            return "movie_id does not exist "

    def delete_movie(self, movie_id):
        filter = {"movie_id": movie_id}
        if movie_collection_info.find_one(filter, {"_id": False}):
            movie_collection_info.delete_one(filter)
            return "successfully deleted"
        else:
            return "movie id does not  exist "

    def check_person_ID(self, persons_info):
        result = []
        for infoID in persons_info:
            person = check_user_ID(infoID)
            if person:
                result.append(person)
            else:
                return int(infoID)
        return result


def check_thread(thread):
    if movie_collection_info.find_one({"thread": thread}):
        return True
    else:
        return False
