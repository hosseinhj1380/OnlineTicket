from databases import users_collection
from core.hash import Hash


class UserCRUD:
    def __init__(self):
        pass

    def create(self, username, email, password, full_name):
        last_user = users_collection.find_one(sort=[("_id", -1)])
        if last_user:
            userID = last_user["userID"] + 1
        else:
            userID = 1
        try:
            users_collection.insert_one(
                {
                    "full_name": full_name,
                    "username": username,
                    "email": email,
                    "password": Hash.bcrypt(password),
                    "userID": userID,
                    "roles":["client"],
                    "state":"active"
                }
            )
            return "user created successfully "
        except Exception as e:
            return {
                "status": "Error",
                "message": "there is a problem while saving data ",
            }

    def update(self,user,userID):
        user_info=users_collection.find_one({"userID":userID}, {'_id': False})
        if user_info:
            user_info["full_name"]=user["full_name"]
            user_info["email"]=user["email"]    
            try:
                users_collection.update_one({"userID": userID},
                                            {"$set": user_info})
                return "success"
            except Exception as e :
                print(e )
                return None
        else:
            return None
        
    def block_user(self , username):
        if check_username(username) :
            user = find_user(username=username)
        
            user_info=users_collection.find_one({"userID":user["userID"]}, {'_id': False})
        
        
            user_info["state"]="block"
            users_collection.update_one({"userID": user["userID"]},
                                        {"$set": user_info})
            
            return "user blocked successfully "
        
        else: return None     
    
    def admin_access(self , username):
        if check_username(username) :
            user = find_user(username=username)
        
            user_info=users_collection.find_one({"userID":user["userID"]}, {'_id': False})
        
        
            user_info["roles"].append("admin")
            users_collection.update_one({"userID": user["userID"]},
                                        {"$set": user_info})
            
            return "user added to admins  successfully "
        
        else: return None             


def check_username(username):
    if users_collection.find_one({"username": username}, {"_id": False}):
        return True
    else:
        return False


def find_user(username):
    
    return users_collection.find_one(
        {"username": username}, {"_id": False, "password": False, "email": False}
    )


def authenticate_user(username):
    return users_collection.find_one(
        {"username": username},
        {"_id": False}
    )

def check_email_not_available(email):
    return users_collection.find_one({"email":email} , {"_id": False})