from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemes.comment_schemas import CreateComment,UpdateComment
from crud.comment_crud import CRUDcommnet,CommentCheck


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

@router.patch("/api/comment/comments/{commentID}")
def update_comment(commentID:int,comment:UpdateComment):
    if comment:
        obj=CRUDcommnet()
        result=obj.update_comment(text=comment.text,commentID=commentID)
        if result is not None:
            return JSONResponse(status_code=200,content= result)
        else:
            return JSONResponse(status_code=404,content="thread not found")

@router.get("/api/comment/pending/")
def unchecked_comment():
    checkcomment=CommentCheck()
    pending_comment=checkcomment.get_all_pending_comment()
    
    if pending_comment :
        return JSONResponse(status_code=200,content=pending_comment)
    else:
        return JSONResponse(status_code=400,content="no pending comment available")


@router.patch("/api/comment/approve/{commentID}")
def approve_comment(commentID:int):
    edit_comment=CommentCheck()
    result=edit_comment.approve_comment(commentID=commentID)
    if result:
        return JSONResponse(status_code=200,content=result)
    else:
        return JSONResponse(status_code=404,content="commentID not found ")
