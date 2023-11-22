from databases import comment_collection
from datetime import datetime
from crud import movies_crud
import json
from .thread import check_thread


class CRUDcommnet:
    def __init__(self):
        pass

    def create_comment(self, text, thread, user):
        last_comment = comment_collection.find_one(sort=[("_id", -1)])
        if last_comment:
            commentID = last_comment["commentID"] + 1
        else:
            commentID = 1

        if check_thread(thread=thread):
            try:
                comment_collection.insert_one(
                    {
                        "commentID": commentID,
                        "user": user,
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
        comment = comment_collection.find_one({"commentID": commentID}, {"_id": False})
        if comment:
            comment["text"] = text
            comment["state"] = "pending"
            comment["created_at"] = str(datetime.now())
            comment_collection.update_one({"commentID": commentID}, {"$set": comment})
            return {"text": text, "status": "pending"}
        else:
            return None

    def movie_comments(self, thread, skip, page_size):
        count = comment_collection.count_documents(
            {"thread": thread, "state": "approved"}
        )
        comments = (
            comment_collection.find(
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

    def get_all_pending_comment(self,skip, page_size):
        comments= comment_collection.find({"state": "pending"}, {"_id": False}).skip(skip).limit(page_size)
        count = count = comment_collection.count_documents(
            {"state": "pending"}
        )
        
        return {"count": count, "comments": list(comments)}
    def change_state_comment(self, commentID, state):
        comment = comment_collection.find_one({"commentID": commentID}, {"_id": False})

        if comment:
            if state == "approved" or "notapproved":
                comment["state"] = state
                comment_collection.update_one(
                    {"commentID": commentID}, {"$set": comment}
                )
                return {"message": "comment state changed  successfully"}
            else:
                return {"message": "state is wrong "}
        else:
            return None
