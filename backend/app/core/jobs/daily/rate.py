
from databases import cinema_collection, rate_collection , movie_collection_info


def process_cinema_rate():
    cinemas_id = cinema_collection.find({}, {"_id": False, "cinemaID": True})

    for cinema in list(cinemas_id):

        count = rate_collection.count_documents(
            {"cinemaID": cinema["cinemaID"]})
        if count != 0:

            faclities = 0
            clean = 0
            image_quality = 0
            hall_quality = 0
            services = 0
            sound_quality = 0
            customer_oriention = 0
            results = rate_collection.find({"cinemaID": cinema["cinemaID"]}, {
                                           "_id": False, "rate": True})
            for res in results:
                rate = res["rate"]
                faclities += rate["faclities"]
                clean += rate["clean"]
                image_quality += rate["image_quality"]
                hall_quality += rate["hall_quality"]
                services += rate["services"]
                sound_quality += rate["sound_quality"]
                customer_oriention += rate["customer_oriention"]
            try:
                cinema_collection.update_one({"cinemaID": cinema["cinemaID"]},  {"$set": {"rate": {"faclities": faclities/count,
                                                                                                   "clean": clean/count,
                                                                                                   "image_quality": image_quality/count,
                                                                                                   "hall_quality": hall_quality/count,
                                                                                                   "services": services/count,
                                                                                                   "sound_quality": sound_quality/count,
                                                                                                   "customer_oriention": customer_oriention/count},
                                                                                          "rate_count": count}})

            except Exception as e:
                print(f"rate process problem {e}")

def process_movie_rate():
    movies_id = movie_collection_info.find({}, {"_id": False, "movie_id": True})
    
    for movie in list(movies_id):
        
        count = rate_collection.count_documents(
            {"movie_id": movie["movie_id"]})
        if count != 0:

            rate = 0

            results = rate_collection.find({"movie_id": movie["movie_id"]}, {
                                           "_id": False, "rate": True})
            for res in results:
                rate += res["rate"]

            try:
                movie_collection_info.update_one({"movie_id": movie["movie_id"]},  {"$set":
                                                                                  {"movie_rate": {
                                                                                      "movie_rate": rate/count,
                                                                                      "rates_count": count}}})

            except Exception as e:

                print(f"rate process problem {e}")