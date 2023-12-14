# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # from sqlalchemy.orm import DeclarativeBase
# # from sqlalchemy.orm import declarativeBase


from pymongo import MongoClient
from dotenv import load_dotenv
import os 
load_dotenv()


DATABASE_HOST=os.environ.get("DATABASE_HOST")
client=MongoClient(DATABASE_HOST)

db = client[os.environ.get("DATABASE_NAME")]

movie_collection_info=db[os.environ.get("MOVIES_COLLECTION_INFO")]

comment_collection=db[os.environ.get("COMMENT_COLLECTION")]

movies_genres_collection=db[os.environ.get("MOVIES_GENRES_COLLECTION")]

movie_category_collection=db[os.environ.get("MOVIE_CATEGORY_COLLECTION")]

persons_collection=db[os.environ.get("PERSON_COLLECTIONS")]

person_role_collection=db[os.environ.get("PERSON_ROLE_COLLECTIONS")]

users_collection=db[os.environ.get("USERS_COLLECTION")]

cinema_collection = db[os.environ.get("CINEMA_COLLECTION")]

thread_collection = db[os.environ.get("THREAD_COLLECTION")]

halls_collection =db[os.environ.get("CINEMA_HALLS")]

sales_chart_collection =db[os.environ.get("SALES_CHART")]

session_collection = db[os.environ.get("SESSIONS_COLLECTION")]

facilities_collection = db[os.environ.get("FACILITIES_COLLECTION")]

rate_collection =db[os.environ.get("RATE_COLLECTION")]

# db=client["online_ticket"]


# # Connects to the SQLite database
# # DATABASE_URL = "postgresql://root:ixPwRm72cxuT8Lzoegq6eUAl@aberama.iran.liara.ir:30140/online-ticket"

# # DATABASE_URL="sqlite:///./db.sqlite3"
# # engine = create_engine('')
# # engine = create_engine(
# #     DATABASE_URL
# # )
# # SessionLocal = sessionmaker(bind=engine)
# # session = Session()

# # class Base (DeclarativeBase):
# #     pass

# # Base = declarative_base()


# # engine = create_engine('postgresql://postgres:postgres@localhost:5432/tiktok')
# # Session = sessionmaker(bind=engine)
# # session = Session()
