# import requests
# import threading
# import time
# import json

# url = "http://127.0.0.1:8000/api/movie/movie_datails/1"
# url2 = "http://127.0.0.1:8000/api/movie/movie_datails/0"
# url3 = "http://127.0.0.1:8000/api/movie/create/"
# url4 = "http://127.0.0.1:8000/api/comment/comments/"  # Replace with your target URL
# # Replace with your target URL
# num_requests = 1000
# threads = []

# start_time = time.time()


# def send_request():
#     try:
#         response = requests.get(url)
#         response1 = requests.get(url2)
#         headers = {"Content-Type": "application/json"}
#         response2 = requests.post(
#             url3,
#             data=json.dumps(
#                 {
#                     "title": "string",
#                     "producers": [1],
#                     "directors": [1],
#                     "actors": [1],
#                     "description": "string",
#                     "review": "string",
#                     "production_year": 0,
#                     "images": ["string"],
#                     "poster": "string",
#                     "movie_type": "string",
#                     "genres": [{}],
#                     "categories": [{}],
#                 }
#             ),
#             headers=headers,
#         )
#         response3 = requests.post(
#             url4,
#             data=json.dumps({"text": "string", "thread": 13}),
#             headers=headers,
#         )
#         response5=requests.get("http://127.0.0.1:8000/api/person/1")
#         # You can add code here to process the response if needed.
#     except requests.exceptions.RequestException as e:
#         print(f"Request failed: {e}")


# for _ in range(num_requests):
#     thread = threading.Thread(target=send_request)
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# end_time = time.time()
# total_time = end_time - start_time

# print(f"Total time taken: {total_time} seconds")

from backend.app.databases import users_collection

users_collection.create_index({ "user_id": 1 }, { "unique" : True })