from model.isoline_geometry import IsolineGeometry


def model_to_tuple_iso_geometry(model: IsolineGeometry):
    return (str(model.get_id()),
            str(model.get_isoline_id()),
            str(model.get_isobata_id()),
            str(model.get_geometry()))


class IsolineGeometryRepo:
    insert_query = """ INSERT INTO "IsolineGeometry"  (
    "idIsolineGeometry",
    "isoline",
    "idIsobata",
    "geometry") VALUES (%s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_isoline_geometry(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_iso_geometry(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()