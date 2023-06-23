class CompositionPart:

    def __init__(self):
        self._part_id = None
        self._geo_unit = None
        self._lithology_value1 = None
        self._lithology_value2 = None
        self._composition_part_role_value1 = None
        self._composition_part_role_value2 = None

    def get_part_id(self):  # PRIMARY KEY
        return self._part_id

    def set_part_id(self, part_id):
        self._part_id = part_id

    def get_geo_unit(self):  # FOREIGN KEY
        return self._geo_unit

    def set_geo_unit(self, geo_unit):
        self._geo_unit = geo_unit

    def get_lithology_value1(self):
        return self._lithology_value1

    def set_lithology_value1(self, material):
        self._lithology_value1 = material

    def get_lithology_value2(self):
        return self._lithology_value2

    def set_lithology_value2(self, material):
        self._lithology_value2 = material

    def get_composition_part_role_value1(self):
        return self._composition_part_role_value1

    def set_composition_part_role_value1(self, role):
        self._composition_part_role_value1 = role

    def get_composition_part_role_value2(self):
        return self._composition_part_role_value2

    def set_composition_part_role_value2(self, role):
        self._composition_part_role_value2 = role
