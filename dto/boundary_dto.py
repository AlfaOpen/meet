class BoundaryDto:

    def __init__(self):
        self._boundary_id = None
        self._name = None
        self._contact_type = None
        self._geo_unit = None

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_boundary_id(self):
        return self._boundary_id

    def set_boundary_id(self, boundary_id):
        self._boundary_id = boundary_id

    def set_contact_type(self, contact_type):
        self._contact_type = contact_type

    def get_contact_type(self):
        return self._contact_type

    def get_geo_unit(self):
        return self._geo_unit

    def set_geo_unit(self, geo_unit):
        self._geo_unit = geo_unit


