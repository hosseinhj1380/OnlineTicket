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
                }
            )
            return "user created successfully "
        except Exception as e:
            return {
                "status": "Error",
                "message": "there is a problem while saving data ",
            }

    # def update(self,user):


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
    return users_collection.find_one({"username": username}, {"_id": False})
