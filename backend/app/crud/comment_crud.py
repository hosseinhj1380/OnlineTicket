
from databases import movies_comment_collection
from datetime import datetime
from crud import movies_crud
import json

class CRUDcommnet:

    def __init__(self) -> None:
        pass

    def create_thread(self):
        last_thread = movies_comment_collection.find_one(sort=[('_id', -1)])
        
        if last_thread:
            thread = last_thread["thread"]+1
            movies_comment_collection.insert_one({
                "thread":thread,
                "result":[]
            })
        else:
            thread = 1
            movies_comment_collection.insert_one({
                "thread":thread,
                "result":[]
            })
        return thread

    def create_comment(self,text,thread):

        if movies_crud.check_thread(thread=thread):
            try:
                
                movies_comment_collection.insert_one({
                    "commentID":1,
                    "user":{},
                    "text":text,
                    "created_at":str(datetime.now()),
                    "state":"pending",
                    "likes_count":0,
                    "dislike_count":0,
                    "replies_count":0,
                    "replies":[],
                    "thread":thread
                })
                
                return ({"text":text,"status":"pending"})

            except  :
            
                return("create_comment failed while save ")
                    
        else:
            return(None)


    def update_comment(self,text,commentID):
        comment=movies_comment_collection.find_one({"commentID":commentID}, {'_id': False})
        if comment:
            comment["text"]=text
            comment["state"]="pending"
            comment["created_at"]=str(datetime.now())
            movies_comment_collection.update_one(
            {"commentID":commentID},
            {"$set":comment})
            return {"text":text,"status":"pending"}
        else:
            return None