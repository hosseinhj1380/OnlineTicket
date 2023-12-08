from databases import movie_collection_info ,sales_chart_collection
from datetime import datetime

def process_sales_chart():
    pipeline = [
        {"$sort": {"has_been_sold": -1}},
        {
            "$project": {
                "_id": 0,
                "movie_id": 1,
                "has_been_sold": True,
                "title": "$movie_info.title",
                "producers": "$movie_info.producers",
            }
        },
    ]

    result = list(movie_collection_info.aggregate(pipeline))

    sales_chart_collection.insert_one(
        {"sales_chart": result, "process_date": str(datetime.now())}
    )
