
from databases import movies_comment_collection


class CRUDcommnet:

    def __init__(self):
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
