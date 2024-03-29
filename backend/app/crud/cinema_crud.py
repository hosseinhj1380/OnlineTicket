from databases import cinema_collection, halls_collection, session_collection , rate_collection
from .thread import create_thread
from .movies_crud import CRUDmovies
from core.parameters_check import is_valid_format
from datetime import date, datetime, timedelta, timezone
from .facilities_crud import check_facility


class CRUDcinema:
    def __init__(self):
        pass

    def return_error(self, title, name):
        return {"status": "Error", "message": f"{title}: {name} are not available "}

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

                for faci in cinema["facility"]:
                    if check_facility(facility=faci):
                        pass
                    else:
                        return self.return_error(title="facilities", name=faci)
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
            if cinema["facility"]:
                for faci in cinema["facility"]:
                    if check_facility(facility=faci):
                        pass
                    else:
                        return self.return_error(title="facilities", name=faci)

            try:
                cinema_collection.update_one({"cinemaID": cinemaID}, {"$set": cinema})
                return "informations successfully updated "
            except Exception as e:
                return e
        else:
            return None

    def get(self, cinemaID):
        return cinema_collection.find_one({"cinemaID": cinemaID}, {"_id": False})
    

    def get_all_ids(self):
        lst=[]
        lst = cinema_collection.find({},{"_id":False,"cinemaID":True})
        return lst
    

    def get_a_cinema_details(self, cinemaID):
        cinema = cinema_collection.find_one(
            {"cinemaID": cinemaID, "verified": True}, {"_id": False}
        )
        if cinema:
            sort_by_halls = {}
            sort_by_session = {}

            for hallID in cinema["halls"]:
                hall_info = halls_collection.find_one(
                    {
                        "hallID": hallID,
                        "sessions": {"$elemMatch": {"is_active": True}},
                    },
                    {"_id": False, "capacity": False},
                )
                if hall_info is not None:
                    temp = []


                    s = session_collection.find_one(
                        {"sessionID": session["sessionID"], "can_order": True},
                        {"_id": False},
                    )
                    if s is not None:
                        dates = process_start_end_date(
                            start=str(date.today()),
                            end=s["end_release_date"],
                            start_release=s["start_release_date"],
                        )
                        for d in dates:
                            new_Session = {s["sessionID"]: s}
                            temp.append(new_Session)

                            if d not in sort_by_session:
                                sort_by_session[d] = {}

                            sort_by_session[d][s["sessionID"]] = {
                                "halls": {
                                    "min_price": hall_info["min_price"],
                                    "max_price": hall_info["max_price"],
                                    "hallID": hall_info["hallID"],
                                    # "cinemaID": hall_info["cinemaID"],
                                },
                                "session": s,
                            }

                            # del hall_info["cinemaID"]

                            hall_info["sessions"] = temp
                            if hallID not in sort_by_halls:
                                sort_by_halls[hallID] = {
                                    "min_price": hall_info["min_price"],
                                    "max_price": hall_info["max_price"],
                                }

                            sort_by_halls[hallID][s["sessionID"]] = s


            return {
                "cinema": cinema,
                "halls": sort_by_halls,
                "sessions": sort_by_session,
            }

    def new_rate(self , cinemaID , rate):
        if cinema_collection.find_one({"cinemaID":cinemaID} , {"_id": False}):
            rate_collection.insert_one({"cinemaID":cinemaID ,"rate":rate})
            return "success" 
        else: return None        

    def home_cinemas(self, skip, page_size, city):
        count = cinema_collection.count_documents({"city": city, "verified": True})
        cinemas = (
            cinema_collection.find(
                {"city": city, "verified": True},
                {
                    "name": True,
                    "images": True,
                    "facility": True,
                    "rate": True,
                    "rate_count": True,
                    "cinemaID": True,
                    "address": True,
                    "_id": False,
                },
                sort=[("cinemaID")],
            )
            .skip(skip)
            .limit(page_size)
        )

        return {"count": count, "results": list(cinemas)}





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


class CRUDsession:
    def __init__(self):
        pass

    def create(self, cinemaID, hallID, session):
        info = halls_collection.find_one(
            {"hallID": hallID, "cinemaID": cinemaID}, {"_id": False}
        )

        if info:
            c = CRUDmovies()
            movie = c.movie_details(movie_id=session["movieID"])
            if movie:
                try:
                    last_session = session_collection.find_one(sort=[("_id", -1)])

                    if last_session:
                        sessionID = last_session["sessionID"] + 1

                    else:
                        sessionID = 1
                    temp = info["sessions"]

                    temp.append(
                        {
                            "sessionID": sessionID,
                            "is_active": True,
                        }
                    )
                    info["sessions"] = temp

                    halls_collection.update_one({"hallID": hallID}, {"$set": info})
                    session_collection.insert_one(
                        {
                            "sessionID": sessionID,
                            "movie": movie,
                            "start_at": session["start_at"],
                            "start_release_date": session["start_release_date"],
                            "end_release_date": session["end_release_date"],
                            "can_order": True,
                            "cinemaID": info["cinemaID"],
                            "hallID": info["hallID"],
                            "is_active":True
                        }
                    )

                    return " successfully added "
                except Exception as e:
                    return e
            else:
                return "no availabale movie with this id "

        else:
            return None

    def update(self, session):
        info = session_collection.find_one(
            {"sessionID": session["sessionID"]}, {"_id": False}
        )
        if info:
            c = CRUDmovies()
            movie = c.movie_details(movie_id=session["movieID"])
            if movie:
                try:
                    new_session = {
                        "sessionID": info["sessionID"],
                        "movie": movie,
                        "start_at": session["start_at"],
                        "start_release_date": session["start_release_date"],
                        "end_release_date": session["end_release_date"],
                        "can_order": True,
                        "cinemaID": info["cinemaID"],
                        "hallID": info["hallID"],
                    }

                    session_collection.update_one(
                        {"sessionID": session["sessionID"]}, {"$set": new_session}
                    )
                    return " successfully added "
                except Exception as e:
                    return e

            else:
                return "no availabale movie with this id "

        else:
            return None
        
    def check_not_two_session_in_a_time(self , movie_id , cinemaID , start_at):
        sess=session_collection.find_one({"cinemaID":cinemaID,"movie.movie_id":movie_id} , {"_id":False})
        if sess:
            if int(sess["start_at"][:2]) == start_at:
                return False
            else:
                return True
        
        return True       
        
    def delete_session(self, sessionID):
        pass
    
    
        


def process_start_end_date(start, end, start_release):
    start_release_date = datetime.fromisoformat(str(start_release)[:-6])
    current_time = datetime.now(start_release_date.tzinfo)

    if current_time < start_release_date:
        start_date = start_release_date

    else:
        start_date = datetime.fromisoformat(start)

    now_time = datetime.now(timezone(timedelta(hours=3, minutes=30)))
    now_time_format = datetime.fromisoformat(str(now_time)[:-6])

    end_date = datetime.fromisoformat(end[:-6])

    date_list = []
    for x in range((end_date - start_date).days + 1):
        if x == 0:
            if (start_date - now_time_format).seconds >= 3600:
                date_list.append(start_date + timedelta(days=x))

        else:
            date_list.append(start_date + timedelta(days=x))

    return [date.strftime("%Y-%m-%d") for date in date_list]


