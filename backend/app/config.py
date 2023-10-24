from fastapi import FastAPI
from routers import movies_router,genres_router,category_router,comments_router,persons


app = FastAPI()
app.include_router(movies_router.router, tags=["movie"])
app.include_router(genres_router.router,tags=["genres"])
app.include_router(category_router.router,tags=["category"])
app.include_router(comments_router.router,tags=["comment"])
app.include_router(persons.router,tags=["persons"])

