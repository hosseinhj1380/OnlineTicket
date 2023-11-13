from databases import movie_category_collection


class CRUDCategory:
    def __init__(self) -> None:
        pass

    def check_category_availability(self, category_name):
        if movie_category_collection.find_one({"name": category_name}):
            return True
        else:
            return False

    def create_category(self, new_category_name):
        if self.check_category_availability(category_name=new_category_name):
            return "category already is available"
        else:
            try:
                last_category = movie_category_collection.find_one(sort=[("_id", -1)])

                if last_category:
                    category_id = last_category["id"] + 1
                else:
                    category_id = 1

                movie_category_collection.insert_one(
                    {"id": category_id, "name": new_category_name}
                )

                return f"category {new_category_name}  added successfully "

            except:
                return None

    def get_category_details(self):
        return movie_category_collection.find({}, {"name": 1, "id": 1, "_id": 0})

    def update_category(self, category_new_name, category_name):
        if self.check_category_availability(category_name=category_name):
            try:
                movie_category_collection.update_one(
                    {"name": category_name}, {"$set": {"name": category_new_name}}
                )
                return "Successfully Updated "

            except:
                return "Failed to update category"

        else:
            return "category_name doesnt exist "

    def delete_category(self, category_name):
        if self.check_category_availability(category_name=category_name):
            movie_category_collection.delete_one({"name": category_name})
            return "successfully deleted"
        else:
            return "category doesnt exist "


def check_category(category):
    if movie_category_collection.find_one(category):
        return True
    else:
        return False
