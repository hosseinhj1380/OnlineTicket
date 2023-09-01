from fastapi import FastAPI
from routers import movies_router


app = FastAPI()
app.include_router(movies_router.router, tags=["movie"])
