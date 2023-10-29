from databases import movies_comment_collection
from datetime import datetime
from crud import movies_crud
import json


class CRUDcommnet:
    def __init__(self) -> None:
        pass


    

    def create_comment(self, text, thread):
        last_comment = movies_comment_collection.find_one(sort=[("_id", -1)])
        if last_comment:


    def create_comment(self, text, thread):
        last_comment = movies_comment_collection.find_one(sort=[("_id", -1)])
        if last_comment["result"]:

            commentID = last_comment["commentID"] + 1
        else:
            commentID = 1

        if movies_crud.check_thread(thread=thread):
            try:
                movies_comment_collection.insert_one(
                    {
                        "commentID": commentID,
                        "user": {},
                        "text": text,
                        "created_at": str(datetime.now()),
                        "state": "pending",
                        "likes_count": 0,
                        "dislike_count": 0,
                        "replies_count": 0,
                        "replies": [],
                        "thread": thread,
                    }
                )

                return {"text": text, "status": "pending"}

            except:
                return "create_comment failed while save "

        else:
            return None

    def update_comment(self, text, commentID):
        comment = movies_comment_collection.find_one(
            {"commentID": commentID}, {"_id": False}
        )
        if comment:
            comment["text"] = text
            comment["state"] = "pending"
            comment["created_at"] = str(datetime.now())
            movies_comment_collection.update_one(
                {"commentID": commentID}, {"$set": comment}
            )
            return {"text": text, "status": "pending"}
        else:
            return None

    def movie_comments(self, thread, skip, page_size):
        count = movies_comment_collection.count_documents(
            {"thread": thread, "state": "approved"}
        )
        comments = (
            movies_comment_collection.find(
                {"thread": thread, "state": "approved"}, {"_id": False}
            )
            .skip(skip)
            .limit(page_size)
        )

        comments = list(comments)

        return {"count": count, "comments": comments}


class CommentCheck:
    def __init__(self):
        pass

    def get_all_pending_comment(self):
        comments = movies_comment_collection.find({"state": "pending"}, {"_id": False})

        result = []
        if comments:
            for comment in comments:
                result.append(comment)
            return result

        else:
            return None

    def change_state_comment(self, commentID, state):
        comment = movies_comment_collection.find_one(
            {"commentID": commentID}, {"_id": False}
        )

        if comment:
            if state == "approved" or "notapproved":
                comment["state"] = state
                movies_comment_collection.update_one(
                    {"commentID": commentID}, {"$set": comment}
                )
                return {"message": "comment state changed  successfully"}
            else:
                return {"message": "state is wrong "}
        else:
            return None
