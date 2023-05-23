from model.faults_all_3d import FaultsAll3d


def model_to_tuple_faults_all_3d(model: FaultsAll3d):
    return (str(model.get_id()),
            str(model.get_fault_id()),
            str(model.get_x()),
            str(model.get_y()),
            str(model.get_depth()),
            str(model.get_local_name()))


class FaultsAll3dRepo:
    insert_query = """ INSERT INTO "FaultsAll3d"  (
    "id",
    "faultId",
    "x",
    "y",
    "depth",
    "localName") VALUES (%s, %s, %s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_faults_all_3d(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_faults_all_3d(i)
            print (type(values))
            cursor.execute(self.insert_query, values)
        self.connection.commit()