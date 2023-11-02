from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from schemas.comment import CreateComment, UpdateComment
from schemas.users import UserBase
from crud.comment_crud import CRUDcommnet, CommentCheck
from fastapi import Query
from core.auth.oauth2 import get_current_user


router = APIRouter()


@router.post("/api/comment/comments/")
def create_new_commnet(
    comment: CreateComment, 
    current_user: UserBase = Depends(get_current_user)
):
    if comment:
        obj = CRUDcommnet()
        result = obj.create_comment(
            text=comment.text, 
            thread=comment.thread, 
            user=current_user
        )
        if result is not None:
            return JSONResponse(status_code=200, content=result)
        else:
            return JSONResponse(status_code=404, content="thread not found")


@router.patch("/api/comment/comments/{commentID}")
def update_comment(commentID: int, comment: UpdateComment):
    if comment:
        obj = CRUDcommnet()
        result = obj.update_comment(text=comment.text, commentID=commentID)
        if result is not None:
            return JSONResponse(status_code=200, content=result)
        else:
            return JSONResponse(status_code=404, content="thread not found")


@router.get("/api/comment/pending/")
def unchecked_comment():
    checkcomment = CommentCheck()
    pending_comment = checkcomment.get_all_pending_comment()

    if pending_comment:
        return JSONResponse(status_code=200, content=pending_comment)
    else:
        return JSONResponse(status_code=400, content="no pending comment available")


@router.patch("/api/comment/state/{commentID}")
def approve_comment(commentID: int, state: str):
    edit_comment = CommentCheck()
    result = edit_comment.change_state_comment(commentID=commentID, state=state)
    if result:
        return JSONResponse(status_code=200, content=result)
    else:
        return JSONResponse(status_code=404, content="commentID not found ")


@router.get("/api/comment/comments/")
def movie_comments(
    thread: int, page: int = Query(default=1, description="Page number", ge=1)
):
    page_size = 2
    skip = (page - 1) * page_size

    comments = CRUDcommnet()
    result = comments.movie_comments(thread=thread, page_size=page_size, skip=skip)

    if result["comments"] == []:
        return JSONResponse(status_code=404, content="invalid page")

    else:
        if page == 1:
            previous = None
        else:
            previous = (
                f"127.0.0.1:8000/api/comment/comments/?thread={thread}&page={page - 1}"
            )

        if page_size * page < result["count"]:
            next = (
                f"127.0.0.1:8000/api/comment/comments/?thread={thread}&page={page + 1}"
            )

        else:
            next = None

        return JSONResponse(
            status_code=200,
            content={
                "count": result["count"],
                "previous": previous,
                "next": next,
                "comments": result["comments"],
            },
        )
