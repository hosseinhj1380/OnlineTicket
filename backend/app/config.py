from fastapi import FastAPI
from routers import movies_router,genres_router


app = FastAPI()
app.include_router(movies_router.router, tags=["movie"])
app.include_router(genres_router.router,tags=["genres"])
