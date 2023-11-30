from databases import thread_collection

from datetime import datetime


def create_thread(type):
    last_thread = thread_collection.find_one(sort=[("_id", -1)])

    if last_thread:
        thread = last_thread["thread"] + 1
    else:
        thread = 1

    thread_collection.insert_one(
        {
            "type": type,
            "thread": thread,
            "created_at": str(datetime.now()),
        }
    )

    return thread


def check_thread(thread):
    if thread_collection.find_one({"thread": thread}):
        return True
    else:
        return False
