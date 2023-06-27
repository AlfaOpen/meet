from model.isoline_info import IsolineInfo


def model_to_tuple_iso_info(model: IsolineInfo):
    return (str(model.get_id()),
            str(model.get_geom_id()),
            str(model.get_iso_value()),
            str(model.get_x()),
            str(model.get_y()),
            str(model.get_isobata_id()),
            str(model.get_vertex_index()),
            str(model.get_vertex_part()),
            str(model.get_vertex_part_index()),
            str(model.get_distance()),
            str(model.get_angle()))


class IsolineInfoRepo:
    insert_query = """ INSERT INTO "IsolineInfo"  (
    "id",
    "isolineGeometry",
    "isoValue",
    "x",
    "y",
    "idIsobata",
    "vertexIndex",
    "vertexPart",
    "vertexPartIndex",
    "distance",
    "angle") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_isoline_info(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_iso_info(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()
