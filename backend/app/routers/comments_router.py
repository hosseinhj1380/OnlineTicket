from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemes.comment_schemas import CreateComment,UpdateComment
from crud.comment_crud import CRUDcommnet


router = APIRouter()

@router.post("/api/comment/comments/")
def create_new_commnet(comment:CreateComment):
    if comment:
        obj=CRUDcommnet()
        result=obj.create_comment(text=comment.text,thread=comment.thread)
        if result is not None:
            return JSONResponse(status_code=200,content= result)
        else:
            return JSONResponse(status_code=404,content="thread not found")

@router.put("/api/comment/comments/")
def update_comment(comment:UpdateComment):
    if comment:
        obj=CRUDcommnet()
        result=obj.update_comment()
        if result is not None:
            return JSONResponse(status_code=200,content= result)
        else:
            return JSONResponse(status_code=404,content="thread not found")