from elastic_connection import connection


client , index = connection()

def search(text):
    query_cinema = {
    "query": {
        "bool": {
            "must": [
                {
                    "match_phrase": {
                        "type": {
                            "query": "cinema"
                        }
                    }
                },
                {
                    "prefix": {
                        "name": text
                    }
                }
            ]
        }
    }
}
    response = client.search(index=index, body=query_cinema)
    hits_cinemas = response["hits"]["hits"]

    query_movies = {
    "query": {
        "bool": {
            "must": [
                {
                    "match_phrase": {
                        "type": {
                            "query": "cinema"
                        }
                    }
                },
                {
                    "prefix": {
                        "name": text
                    }
                }
            ]
        }
    }
}
    response = client.search(index=index, body=query_movies)
    hits_movies = response["hits"]["hits"]

    return hits_cinemas ,hits_movies