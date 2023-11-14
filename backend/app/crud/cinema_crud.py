from databases import cinema_collection


class CRUDcinema:
    
    def __init__(self) :
        pass
    
    def create(self , cinema):
        if cinema_collection.find_one({"name":cinema["name"]} , {"_id": False}): 
            return None
        else : 
            try :
                
                last_id = cinema_collection.find_one(sort=[("_id", -1)])
                if last_id:
                    cinemaID = last_id["cinemaID"] + 1
                else:
                    cinemaID = 1
                cinema["rate"] = 0 
                cinema["cinemaID"] = cinemaID
                
                cinema_collection.insert_one(cinema)
                return "cinema successfully added "
            except Exception as e :
                return e 
            
            
            

