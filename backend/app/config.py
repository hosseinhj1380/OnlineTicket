from fastapi import FastAPI
from routers import movies,category,comments,genres,persons,users


app = FastAPI()
app.include_router(movies.router, tags=["movie"])
app.include_router(genres.router,tags=["genres"])
app.include_router(category.router,tags=["category"])
app.include_router(comments.router,tags=["comment"])
app.include_router(persons.router,tags=["persons"])
app.include_router(users.router,tags=["user"])


