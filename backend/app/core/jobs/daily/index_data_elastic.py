from crud.cinema_crud import CRUDcinema
from backend.app.core.elastic.indexing import index_cinema_datas , index_movies_data
from crud.movies_crud import CRUDmovies



def index_cinema_info():

    obj = CRUDcinema()

    cinema_IDs = obj.get_all_ids()

    for id in cinema_IDs:
        res = obj.get_a_cinema_details(cinemaID=id)

        response = index_cinema_datas(
            **{
                "name": res["name"],
                "is_active": res["is_active"],
                "id": id,
                "url": f"/api/cinemas/{id}",
            }
        )

        if response["_shards"]["successful"]:
            pass
        else:
            pass
            # LOGGING AND HINT TO ADMINS


def index_movies_info():
    
    obj =CRUDmovies()

    movie_IDs = obj.get_movie_Ids()

    for id in movie_IDs:
        res = obj.get_a_cinema_details(cinemaID=id)

        response = index_movies_data(
            **{
                "name": res["movie_info"]["is_active"],
                "is_active": res["is_active"],
                "id": id,
                "url": f"/api/movie_datails/{id}",
            }
        )

        if response["_shards"]["successful"]:
            pass
        else:
            pass
            # LOGGING AND HINT TO ADMINS
