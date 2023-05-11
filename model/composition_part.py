class CompositionPart:

    def __init__(self):
        self._part_id = None
        self._geo_unit = None
        self._material = None
        self._role = None

    def get_part_id(self):  # PRIMARY KEY
        if self._part_id == 0:
            return "Not Present"
        return self._part_id

    def set_part_id(self, part_id):
        self._part_id = part_id

    def get_geo_unit(self):  # FOREIGN KEY
        if self._geo_unit == 0:
            return "Not Present"
        return self._geo_unit

    def set_geo_unit(self, geo_unit):
        self._geo_unit = geo_unit

    def get_material(self):
        return self._material

    def set_material(self, material):
        self._material = material

    def get_role(self):
        return self._role

    def set_role(self, role):
        self._role = role

