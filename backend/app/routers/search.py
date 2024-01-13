from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from core.elastic.searching import search
from core.jobs.daily.index_data_elastic import index_cinema_info,index_movies_info
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()

scheduler.add_job(index_movies_info, "cron", hour=3, minute=00)
scheduler.add_job(index_cinema_info, "cron", hour=4, minute=00)


router = APIRouter(prefix="/api/search")

@router.get("/")
def search(text:str):
    if text:
        result=search(text)

        return JSONResponse(content=result,status_code=200)
    else:
        return JSONResponse(content=None,status_code=400)