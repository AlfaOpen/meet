from model.isoline_info import IsolineInfo


def model_to_tuple_iso_info(model: IsolineInfo):
    return (str(model.get_id()),
            str(model.get_isoline_id()),
            str(model.get_iso_value()))


class IsolineInfoRepo:
    insert_query = """ INSERT INTO "IsolineInfo"  (
    "id",
    "isoline",
    "isoValue") VALUES (%s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_isoline_info(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_iso_info(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()
