from model.isoline import Isoline


def model_to_tuple_iso(model: Isoline):
    return (str(model.get_isoline_id()),
            model.get_filename(),
            model.get_name(),
            str(model.get_boundary_id()),
            model.get_iso_type())


class IsolineRepo:
    insert_query = """ INSERT INTO "Isoline"  (
    "idIsoline",
    "filename",
    "name",
    "boundaryId",
    "isoType") VALUES (%s, %s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_isoline(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_iso(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()
