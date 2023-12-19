from fastapi import APIRouter, Depends , Query
from fastapi.responses import JSONResponse
from schemas.movies import Movies, MovieUpdate , Rate
from crud.movies_crud import CRUDmovies , sales_chart  ,home_page
from core.auth.oauth2 import oauth2_scheme, is_admin
import base64
from core.jobs.daily.sales_chart import process_sales_chart

from core.jobs.daily.rate import process_movie_rate

from apscheduler.schedulers.background import BackgroundScheduler
# import aioredis
from aioredis import Redis




scheduler = BackgroundScheduler()

scheduler.add_job(process_sales_chart, "cron", hour=00, minute=22)
scheduler.add_job(process_movie_rate, "cron", hour=4, minute=31)

scheduler.start()

async def get_redis():
    redis = await Redis.from_url("redis://localhost",encoding="utf8", decode_responses=True)
    yield redis
    redis.close()
    await redis.wait_closed()

router = APIRouter(prefix="/api/movie")


@router.post("/create/", dependencies=[Depends(is_admin)])
def create_movie_info(movie: Movies, token: str = Depends(oauth2_scheme)):
    if movie:
        #    for movie_picture in movie.movie_images:
        #        try:
        #            decode_image = base64.b64decode(movie_picture)

        #        except:

        #            return JSONResponse(status_code=400, content="movie_images format is not in base64 format ")

        #    try:
        #        decode_image = base64.b64decode(movie.movie_poster)

        #    except:
        #        return JSONResponse(status_code=400, content="movie_poster  format is not in base64 format ")

        movie_dict = movie.dict()
        obj = CRUDmovies()
        result = obj.create_movie(movie_dict)
        if result["status"] == "Success":
            return JSONResponse(status_code=201, content=result)
        else:
            return JSONResponse(status_code=400, content=result)
    else:
        return JSONResponse(status_code=400, content="bad request (value is null )")


@router.get("/movie_datails/{movie_id}")
def get_movie_details(movie_id: int):
    obj = CRUDmovies()
    result = obj.movie_details(movie_id=movie_id)

    if result:
        return JSONResponse(status_code=200, content=result)
    else:
        return JSONResponse(status_code=404, content="movie not found ")


@router.put("/movie_update/", dependencies=[Depends(is_admin)])
def movies_update(movie: MovieUpdate):
    if movie:
        # for movie_picture in  movie.movie_images:
        #     try:
        #         decode_image=base64.b64decode(movie_picture)

        #     except:

        #         return JSONResponse(status_code=400,content="movie_images format is not in base64 format ")

        # try:
        #     decode_image=base64.b64decode(movie.movie_poster)

        # except:
        #         return JSONResponse(status_code=400,content="movie_poster  format is not in base64 format ")
        movie_id = movie.movie_id

    movie_dict = movie.dict()

    obj = CRUDmovies()
    result = obj.movie_update(movie_id=movie_id, movie_info=movie_dict)
    
    if result == "success":
        return JSONResponse(status_code=202, content="updated successfully")
    elif result == "failed":
        return JSONResponse(
            status_code=500, content="internal server error please try later "
        )
    elif result == "movie_id doesnt exist ":
        return JSONResponse(status_code=404, content="movie_id doesnt exist")
    else :
        return JSONResponse(status_code= 406 , content= result)


@router.delete("/movie_delete/{movie_id}", dependencies=[Depends(is_admin)])
def movies_delete(movie_id: int):
    obj = CRUDmovies()
    result = obj.delete_movie(movie_id=movie_id)
    if result == "successfully deleted":
        return JSONResponse(status_code=202, content=result)
    elif result == "movie_id doesnt exist ":
        return JSONResponse(status_code=404, content=result)


@router.get("/sales-chart")
def sales_chart_box(page_size: int,page: int = Query(default=1, description="Page number", ge=1) ):
    
    skip = (page - 1) * page_size
    
    result =sales_chart(skip=skip , page_size=page_size)
    if result["results"] == []:
        return JSONResponse(status_code=404, content="invalid page")

    else:
        if page == 1:
            previous = None
        else:
            previous = (
                f"127.0.0.1:8000/api/cinema/home/?page={page - 1}&page_size={page_size}"
            )

        if page_size * page < result["count"]:
            next = (
                f"127.0.0.1:8000/api/comment/comments/?page={page + 1}&page_size={page_size}"
            )

        else:
            next = None

        return JSONResponse(
            status_code=200,
            content={
                "count": result["count"],
                "previous": previous,
                "next": next,
                "results": result["results"],
            },

        )
        
@router.get("/home")
def movie_homepage(page_size : int, redis: Redis = Depends(get_redis)):
    value = redis.get("home")
    if value:
        return {"value": value }
    else:
        return JSONResponse(status_code=200 , content=home_page(page_size=page_size))
    
    
@router.post("/rate" )
def rate_cinema(movieID: int ,rate :Rate , token: str = Depends(oauth2_scheme)):
    if rate:
        r =CRUDmovies()
        
        result=r.new_rate(movieID=movieID , rate=rate.rate) 
        if result is not None:
            return JSONResponse (status_code=200 , content=result)
        else:
            return JSONResponse(status_code=404 ,content="movie not found ")
        
        


@router.get("/get_from_cache/{key}")
async def get_from_cache(key: str, redis: Redis = Depends(get_redis)):
    value = await redis.get(key)
    return {"key": key, "value": value if value else None}

@router.post("/add_to_cache")
async def add_to_cache(redis: Redis = Depends(get_redis)):
    value=await home_page(page_size=15)
    
    
