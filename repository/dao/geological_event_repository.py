from model.geological_event import GeologicalEvent


def model_to_tuple_geological_event(model: GeologicalEvent):
    return (str(model.get_era_id()),
            str(model.get_geo_unit()),
            model.get_older_named_age(),
            model.get_younger_named_age())


class GeologicalEventRepo:
    insert_query = """ INSERT INTO "GeologicalEvent"  (
    "idEra",
    "geounit",
    "olderNamedAge",
    "YoungerNamedAge") VALUES (%s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_geological_event(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_geological_event(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()

