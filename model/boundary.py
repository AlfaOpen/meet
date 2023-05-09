class Boundary:
    _boundary_id: int
    _name: str
    _contact_type: str
    _geo_unit: str

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_boundary_id(self):
        if self._boundary_id == 0:
            return "Not Present"
        return self._boundary_id

    def set_contact_type(self, contact_type):
        self._contact_type = contact_type

    def get_contact_type(self):
        return self._contact_type

    def get_geo_unit(self):
        return self._geo_unit

    def set_geo_unit(self, geo_unit):
        self._geo_unit = geo_unit
