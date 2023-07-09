from model.boundary_info import BoundaryInfo


def model_to_tuple_boundary_info(model: BoundaryInfo):
    return (str(model.get_id()),
            str(model.get_boundary_id()),
            str(model.get_x()),
            str(model.get_y()),
            str(model.get_depth()),
            (model.get_thickness()),
            str(model.get_geometry()))


class BoundaryInfoRepo:
    insert_query = """ INSERT INTO "BoundaryInfo"  (
    "idInfo3D",
    "boundaryId",
    "x",
    "y",
    "depth",
    "thickness",
    "geometry") VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_boundary_info(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_boundary_info(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()

