
from databases import movies_comment_collection


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

        collection=movies_comment_collection.find_one({"thread": thread}, {'_id': False})
        if collection:
            comment_results=collection["result"]
            new_comment={
                    "id":0,
                    "user":{},
                    "text":text,
                    "created_at":0,
                    "state":"pending",
                    "likes_count":0,
                    "dislike_count":0,
                    "replies_count":0,
                    "replies":[],
                    "thread":thread
            }
            comment_results.append(new_comment)

            try:
                movies_comment_collection.update_one(
                    {"thread": thread},
                    {"$set": {"thread": thread,
                              "result":comment_results}})
                return (new_comment)
            except :
                return("create_comment failed while save ")
                

        else:
            return(None)
