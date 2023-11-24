from databases import cinema_collection, halls_collection
from .thread import create_thread
from .movies_crud import CRUDmovies
from core.parameters_check import is_valid_format
from datetime import date


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

    def get_a_cinema_details(self, cinemaID):
        cinema = cinema_collection.find_one(
            {"cinemaID": cinemaID, "verified": True}, {"_id": False}
        )
        if cinema:
            sort_by_halls = []
            sort_by_session =[]
            
            for hallID in cinema["halls"]:
                hall_info = halls_collection.find_one(
                    {
                        "hallID": hallID,
                        "sessions": {"$elemMatch": {"can_order": True}},
                    },
                    {"_id": False, "capacity": False, "sessions.is_active": False},
                )
                temp = []
                for session in hall_info["sessions"]:
                    new_Session = {session["sessionID"]: session}
                    temp.append(new_Session)
                    if str(date.today()) in session["start_at"]:
                        
                        
                        sort_by_session.append({
                            session["sessionID"]:
                                {
                                
                                "halls":{"min_price":hall_info["min_price"],
                                         "max_price":hall_info["max_price"],
                                         "hallID":hall_info["hallID"],
                                         "cinemaID":hall_info["cinemaID"],
                                         },
                                "session":new_Session
                            }
                        })
                        
                        
                        
                hall_info["sessions"] = temp
                sort_by_halls.append({hallID: hall_info})
                

                
            

            return {"cinema": cinema, "halls": sort_by_halls,
                    "sessions":sort_by_session}

        else:
            return None


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
                hall["sessions"] = []
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

    def new_session(self, cinemaID, hallID, session):
        info = halls_collection.find_one(
            {"hallID": hallID, "cinemaID": cinemaID}, {"_id": False}
        )

        if info:
            c = CRUDmovies()
            movie = c.movie_details(movie_id=session["movieID"])
            if movie:
                try:
                    sessions = info["sessions"]

                    if sessions:
                        sessionID = sessions[-1]["sessionID"] + 1
                    else:
                        sessionID = 1
                    temp = info["sessions"]

                    temp.append(
                        {
                            "sessionID": sessionID,
                            "movie": {"movie": movie},
                            "start_at": session["start_at"],
                            "can_order": True,
                            "is_active": True,
                        }
                    )
                    info["sessions"] = temp

                    halls_collection.update_one({"hallID": hallID}, {"$set": info})
                    return " successfully added "
                except Exception as e:
                    return e
            else:
                return "no availabale movie with this id "

        else:
            return None

    def update_session(self, cinemaID, hallID, session):
        info = halls_collection.find_one(
            {"hallID": hallID, "cinemaID": cinemaID}, {"_id": False}
        )
        if info:
            sessions = info["sessions"]
            for i in range(len(sessions)):
                if session["sessionID"] == sessions[i]["sessionID"]:
                    c = CRUDmovies()
                    movie = c.movie_details(movie_id=session["movieID"])
                    if movie:
                        try:
                            sessions[i] = {
                                "sessionID": session["sessionID"],
                                "movie": {"movie": movie},
                                "start_at": session["start_at"],
                                "can_order": True,
                                "is_active": True,
                            }

                            info["sessions"] = sessions

                            halls_collection.update_one(
                                {"hallID": hallID}, {"$set": info}
                            )
                            return " successfully added "
                        except Exception as e:
                            return e

                    else:
                        return "no availabale movie with this id "

            return "invalid sessionId"
        else:
            return None

    def delete_session(self, sessionID):
        pass
