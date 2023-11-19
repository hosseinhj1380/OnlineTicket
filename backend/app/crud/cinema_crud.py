from databases import cinema_collection, halls_collection
from .thread import create_thread


class CRUDcinema:
    def __init__(self):
        pass

    def create(self, cinema):
        if cinema_collection.find_one({"name": cinema["name"]}, {"_id": False}):
            return None
        else:
            try:
                thread = create_thread("cinema")

                last_id = cinema_collection.find_one(sort=[("_id", -1)])
                if last_id:
                    cinemaID = last_id["cinemaID"] + 1
                else:
                    cinemaID = 1
                cinema["rate"] = 0
                cinema["thread"] = thread
                cinema["rate_count"] = 0
                cinema["halls_count"] = 0
                cinema["verified"] = False
                cinema["halls"] = []

                cinema["cinemaID"] = cinemaID

                cinema_collection.insert_one(cinema)
                return "cinema successfully added "
            except Exception as e:
                return e

    def update(self, cinemaID, cinema):
        cinema_info = cinema_collection.find_one({"cinemaID": cinemaID}, {"_id": False})
        if cinema_info:
            try:
                cinema_collection.update_one({"cinemaID": cinemaID}, {"$set": cinema})
                return "informations successfully updated "
            except Exception as e:
                return e
        else:
            return None

    def get(self, cinemaID):
        return cinema_collection.find_one({"cinemaID": cinemaID}, {"_id": False})


class CRUDhalls:
    def __init__(self):
        pass

    def create(self, cinemaID, hall):
        cinema = cinema_collection.find_one({"cinemaID": cinemaID}, {"_id": False})
        if cinema:
            last = halls_collection.find_one(sort=[("_id", -1)])
            if last:
                hallid = last["hallID"] + 1
            else:
                hallid = 1
            try:
                available_halls = cinema["halls"]
                available_halls.append(hallid)
                cinema["halls"] = available_halls
                cinema_collection.update_one({"cinemaID": cinemaID}, {"$set": cinema})
                hall["hallID"] = hallid
                hall["cinemaID"] = cinemaID
                halls_collection.insert_one(hall)

                return " successfully added "
            except Exception as e:
                return e

        else:
            return None

    def update(self, cinemaID, hallID, hall):
        h = halls_collection.find_one({"hallID": hallID}, {"_id": False})
        c = cinema_collection.find_one({"cinemaID": cinemaID}, {"_id": False})
        if h and c:
            if hallID in c["halls"]:
                halls_collection.update_one({"hallID": hallID}, {"$set": hall})
                return " successfully updated "
            else:
                return " this hall doesnt assign to this cinema "
        else:
            return None

    def get(self, cinemaID, hallID=None):
        if hallID is None:
            return halls_collection.find({"cinemaID": cinemaID}, {"_id": False})

        else:
            return halls_collection.find_one(
                {"cinemaID": cinemaID, "hallID": hallID}, {"_id": False}
            )
