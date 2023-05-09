class CompositionPart:
    _part_id: int
    _geo_unit: str
    _material: str
    _role: str

    def get_part_id (self):
        if self._part_id == 0:
            return "Not Present"
        return self._part_id

    def set_geo_unit (self, geo_unit):   #stessa di bounaryID, è un problema?
        self._geo_unit = geo_unit

    def get_geo_unit (self):
        return self._geo_unit

    def get_material(self):
        return self._material

    def set_material(self, material):
        self._material = material

    def get_role(self):
        return self._role

    def set_role(self, role):
        self._role = role