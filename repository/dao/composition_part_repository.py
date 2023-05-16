from model.composition_part import CompositionPart


def model_to_tuple_composition_part(model: CompositionPart):
    return (str(model.get_part_id()),
            str(model.get_geo_unit()),
            model.get_lithology_value1(),
            model.get_lithology_value2(),
            model.get_composition_part_role_value1(),
            model.get_composition_part_role_value2())


class CompositionPartRepo:
    insert_query = """ INSERT INTO "CompositionPart"  (
    "idPart",
    "geounit",
    "Material1",
    "Material2",
    "Role1",
    "Role2") VALUES (%s, %s, %s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_composition_part(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_composition_part(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()
