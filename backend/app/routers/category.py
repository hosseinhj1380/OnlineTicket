from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from schemas.category import Category, CategoryUpdate
from crud.category_crud import CRUDCategory
from core.auth.oauth2 import is_admin

router = APIRouter(prefix="/api/category")


@router.post("/create/", dependencies=[Depends(is_admin)])
def create_movies_genres(category: Category):
    if category:
        obj = CRUDCategory()
        result = obj.create_category(new_category_name=category.name)
        if result:
            return JSONResponse(status_code=200, content=result)
        else:
            return JSONResponse(
                status_code=500, content="internal server error try later "
            )

    else:
        return JSONResponse(status_code=400, content="bad request")


@router.get("/details/")
def get_movies_genres():
    obj = CRUDCategory()

    documents = obj.get_category_details()

    return JSONResponse(status_code=200, content=list(documents))


@router.put("/update/", dependencies=[Depends(is_admin)])
def update_movie_genres(new_category: CategoryUpdate):
    if new_category:
        obj = CRUDCategory()
        result = obj.update_category(
            category_name=new_category.name, category_new_name=new_category.new_name
        )
        if result == "Successfully Updated ":
            return JSONResponse(status_code=200, content=result)
        elif result == "Failed to update genres":
            return JSONResponse(status_code=500, content=result)
        else:
            return JSONResponse(status_code=404, content=result)


@router.delete("/delete/{cateory_name}", dependencies=[Depends(is_admin)])
def delete_movies_genres(cateory_name: str):
    obj = CRUDCategory()
    result = obj.delete_category(category_name=cateory_name)
    if result == "successfully deleted":
        return JSONResponse(status_code=200, content=result)
    else:
        return JSONResponse(status_code=404, content=result)
