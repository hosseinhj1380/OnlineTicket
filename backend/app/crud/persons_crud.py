from databases import persons_collection,person_role_collection


class PersonsCRUD:
    def __init__(self) :
        pass
    
    def personID_generator(self):
        
        last_document = persons_collection.find_one(sort=[('_id', -1)])
        
        if last_document:
            personID = last_document["PersonID"]+1
        else:
            personID = 1
            
        
        return {"PersonID":personID}
    
    def create(self,PersonInfo):
        
        try:
            personID=self.personID_generator()
            
            PersonInfo.update(personID)
            for role in PersonInfo.get("roles"):
                if check_role(role=role.get("name"),id=role.get("id")):
                    pass
                else:
                    return {"status":"success",
                    "message":"valueerror"}
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
        
    def update(self,PersonID,PersonInfo):
        
        if persons_collection.find_one({"PersonID":PersonID}, {'_id': False}):
            try:
                
                persons_collection.update_one({"PersonID": PersonID},
                                              {"$set": PersonInfo})
                return {"message":"success",
                        "PersonInfo":PersonInfo}
            except Exception as e :
                return( e)
        else:
            return None
        
    def delete(self,PersonID):
        filter={"PersonID":PersonID}
        if persons_collection.find_one(filter, {'_id': False}):
            try:
                persons_collection.delete_one(filter)
                return "deleted successfully "
            except Exception as e:
                return e
        else:
            return None
            
            
class PersonRoleCRUD:
    
    def __init__(self):
        pass
    
    def id_generator(self):
        last_document = person_role_collection.find_one(sort=[('_id', -1)])
        
        if last_document:
            id = last_document["id"]+1
        else:
            id = 1
        return id     
            
    def create(self,role):
        id=self.id_generator()
        person_role_collection.insert_one({"id":id,"role":role})
        
        return "success "
    def get (self):
        
        return list(person_role_collection.find({},{'_id': False}))
    
def check_role(id,role):
    if person_role_collection.find_one({"id":id,"role":role}, {'_id': False}): 
        return True
    else: return False
        
        
def check_user_ID(id):
    person=persons_collection.find_one({"PersonID":id}, {"full_name":True,
                                                         "profile_photo":True,
                                                         "PersonID":True,
                                                         '_id': False})
    if person:
        
        return person
    else: return None