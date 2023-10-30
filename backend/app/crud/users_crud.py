from databases import users_collection
from crud.hash import Hash

class UserCRUD:
    def __init__(self) :
        pass
    
    def create (self,username,email,password):
        try:
            users_collection.insert_one({
            "username":username,
            "email":email,
            "password":Hash.bcrypt(password)
             })
            return "user created successfully "
        except Exception as e :
            print(e)
            
            return  {"status": "Error",
                     "message": "there is a problem while saving data " } 
        
def check_username(username):
    if users_collection.find_one({"username":username},{'_id': False}):
        return True
    else:return False