from model.faults_shp import FaultsShp


def model_to_tuple_faults_shp(model: FaultsShp):
    return (str(model.get_id()),
            model.get_fault_id(),
            str(model.get_x()),
            str(model.get_y()),
            model.get_local_name(),
            (model.get_vertex_index()),
            (model.get_vertex_part()),
            (model.get_vertex_part_index()),
            (model.get_distance()),
            (model.get_angle()))


class FaultsShpRepo:
    insert_query = """ INSERT INTO "FaultsShp"  (
    "id",
    "faultId",
    "x",
    "y",
    "localName",
    "vertexIndex",
    "vertexPart",
    "vertexPartIndex",
    "distance",
    "angle") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_faults_shp(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_faults_shp(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()

