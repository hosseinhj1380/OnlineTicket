headers = {'Content-Type': 'application/json'}
response2 = requests.post(
            url,
            data=json.dumps(
                {
                    "title": "string",
                    "producers": [1],
                    "directors": [1],
                    "actors": [1],
                    "description": "string",
                    "review": "string",
                    "production_year": 0,
                    "images": ["string"],
                    "poster": "string",
                    "movie_type": "string",
                    "genres": [{}],
                    "categories": [{}],
                }
            ),
            headers=headers,
        )