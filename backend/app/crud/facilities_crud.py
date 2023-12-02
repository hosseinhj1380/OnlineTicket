from databases import facilities_collection


class FacilitiesCRUD:
    def __init__(self) -> None:
        pass

    def check_facility_availability(self, facility_name):
        if facilities_collection.find_one({"name": facility_name}):
            return True
        else:
            return False

    def create_facility(self, new_facility_name):
        if self.check_facility_availability(facility_name=new_facility_name):
            return "facility already is available"
        else:
            try:
                last_facility = facilities_collection.find_one(sort=[("_id", -1)])

                if last_facility:
                    facility_id = last_facility["id"] + 1
                else:
                    facility_id = 1

                facilities_collection.insert_one(
                    {"id": facility_id, "name": new_facility_name}
                )

                return f"facility  {new_facility_name}  added successfully "

            except:
                return None

    def get_facility_details(self):
        return facilities_collection.find({}, {"name": 1, "_id": 0})

    def update_facility(self, facility_new_name, facility_name):
        if self.check_facility_availability(facility_name=facility_name):
            try:
                facilities_collection.update_one(
                    {"name": facility_name}, {"$set": {"name": facility_new_name}}
                )
                return "Successfully Updated "

            except:
                return "Failed to update facility"

        else:
            return "facility_name doesnt exist "

    def delete_facility(self, facility_name):
        if self.check_facility_availability(facility_name=facility_name):
            facilities_collection.delete_one({"name": facility_name})
            return "successfully deleted"
        else:
            return "facility doesnt exist "


def check_facility(facility):
    if facilities_collection.find_one({"name": facility}):
        return True
    else:
        return False
