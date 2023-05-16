from model.boundary import Boundary


def model_to_tuple_boundary(model: Boundary):
    return (str(model.get_boundary_id()),
            model.get_name(),
            model.get_contact_type(),
            str(model.get_geo_unit()))


class BoundaryRepo:
    insert_query = """ INSERT INTO "Boundary"  (
    "idBoundary",
    "name",
    "contactType",
    "geounit") VALUES (%s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_boundary(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_boundary(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()