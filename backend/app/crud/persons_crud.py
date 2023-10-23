from databases import persons_collection


class PersonsCRUD:
    def __init__(self) :
        pass
    
    def personID_generator(self):
        
        last_document = persons_collection.find_one(sort=[('_id', -1)])
        print(last_document)
        if last_document:
            personID = last_document["PersonID"]+1
        else:
            personID = 1
            
        print(personID)
        return {"PersonID":personID}
    
    def create(self,PersonInfo):
        
        try:
            personID=self.personID_generator()
            print(personID)
            PersonInfo.update(personID)
            persons_collection.insert_one(PersonInfo)
            
            return {"status":"success",
                    "message":"person saved successfully "}
        
        except Exception as e :
            return {"status":"failed",
                    "message":f"create person failed because this error {e}"}
            
    def get(self,PersonID):
        
        person_info=persons_collection.find_one({"PersonID":PersonID}, {'_id': False})
        if person_info:
            return person_info
        else:
            return None 
        