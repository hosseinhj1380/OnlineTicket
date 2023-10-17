from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemes.comment_schemas import CreateComment


router = APIRouter()

@router.post("/api/comment/comments/")
def create_new_commnet(comment:CreateComment):
    if comment:
        