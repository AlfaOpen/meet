from model.geologic_unit import GeologicUnit


def model_to_tuple_geo(model: GeologicUnit):
    return (str(model.get_geo_unit_id()),
            model.get_name(),
            model.get_description(),
            str(model.get_ref_geo_unit()),
            model.get_geo_unit_type())


class GeologicUnitRepo:
    insert_query = """ INSERT INTO "GeologicUnit"  (
    "inspireId",
    "name",
    "description",
    "refGeoUnit",
    "geologicUnitType") VALUES (%s, %s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_geologic_unit(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_geo(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()
