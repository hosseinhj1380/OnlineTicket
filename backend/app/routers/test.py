from fastapi import Depends, APIRouter, Query
from sqlalchemy.orm import session
from dependencies import get_db


router = APIRouter()




@router.post("/test/")
def create_comment(
    comment_id: int = Query(
        None,
        title="title text",
        description="Description Text !",
        alias="CommentID",
        deprecated=True,
    )
):
    return {"comment_id": comment_id}