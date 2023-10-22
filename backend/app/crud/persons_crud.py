from databases import persons_collection


class PersonsCRUD:
    def __init__(self) -> None:
        pass
    
    def create(self,PersonInfo):
        print(type(PersonInfo))
        try:
            persons_collection.insert_one(PersonInfo)
            
            return {"status":"success",
                    "message":"person saved successfully "}
        
        except Exception as e :
            return {"status":"failed",
                    "message":f"create person failed because this error {e}"}
        
        