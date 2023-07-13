create_query = '''CREATE TABLE IF NOT EXISTS public."CompositionPart1"
    (
    "idPart" integer NOT NULL,
    geoUnit varchar,
    "Material" varchar,
    "Role" varchar,
    CONSTRAINT "CompositionPart1_pkey" PRIMARY KEY ("idPart"),
    CONSTRAINT "CompositionPart1_geoUnit_fkey" FOREIGN KEY (geoUnit)
        REFERENCES public."GeologicUnit" ("inspireId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."CompositionPart1"
        OWNER to giulia;'''

    # cursor = opened_connection.connection.cursor()
    # cursor.execute(create_query)
    # opened_connection.connection.commit()



class CompositionPart1Dto:

    def __init__(self):
        self._part_id = None
        self._geo_unit = None
        self._lithology_value = None
        self._role_value = None

    def get_part_id(self):  # PRIMARY KEY
        return self._part_id

    def set_part_id(self, part_id):
        self._part_id = part_id

    def get_geo_unit(self):  # FOREIGN KEY
        return self._geo_unit

    def set_geo_unit(self, geo_unit):
        self._geo_unit = geo_unit

    def get_lithology_value(self):
        return self._lithology_value

    def set_lithology_value(self, material):
        self._lithology_value = material

    def get_role_value(self):
        return self._role_value

    def set_role_value(self, role):
        self._role_value = role

class CompositionPart1:

    def __init__(self):
        self._part_id = None
        self._geo_unit = None
        self._lithology_value = None
        self._role_value = None

    def get_part_id(self):  # PRIMARY KEY
        return self._part_id

    def set_part_id(self, part_id):
        self._part_id = part_id

    def get_geo_unit(self):  # FOREIGN KEY
        return self._geo_unit

    def set_geo_unit(self, geo_unit):
        self._geo_unit = geo_unit

    def get_lithology_value(self):
        return self._lithology_value

    def set_lithology_value(self, material):
        self._lithology_value = material

    def get_role_value(self):
        return self._role_value

    def set_role_value(self, role):
        self._role_value = role


class CompositionPart1Mapper:

    def to_model(self, composition_part_dto):
        composition_part = CompositionPart1()
        composition_part.set_part_id(composition_part_dto.get_part_id())
        composition_part.set_geo_unit(composition_part_dto.get_geo_unit())
        composition_part.set_lithology_value(composition_part_dto.get_lithology_value())
        composition_part.set_role_value(composition_part_dto.get_role_value())
        return composition_part

    def to_model_list_composition_part1(self, list_composition_part_dto: list):
        model_list = []
        for dto in list_composition_part_dto:
            model_list.append(self.to_model(dto))
        return model_list


def model_to_tuple_composition_part1(model: CompositionPart1):
    return (str(model.get_part_id()),
            str(model.get_geo_unit()),
            model.get_lithology_value(),
            model.get_role_value())


class CompositionPart1Repo:
    insert_query = """ INSERT INTO "CompositionPart1"  (
    "idPart",
    "geounit",
    "Material",
    "Role") VALUES (%s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_composition_part1(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_composition_part1(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()


tabled = dynamic_load.to_dto(
    r"C:\Users\giuli\Desktop\ISPRA\Test_Dataset_PoBasin\tabelle\CompositionPart1.xlsx", "CompositionPart1Dto",
    [0, 1, 3, 4])
print(tabled)
composition_part1_mapper = CompositionPart1Mapper()
models = composition_part1_mapper.to_model_list_composition_part1(tabled)
print(models)
comppart_repo = CompositionPart1Repo(opened_connection.connection)
comppart_repo.populate_composition_part1(models)