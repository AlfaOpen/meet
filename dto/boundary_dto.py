class BoundaryDto:
    def __init__(self, boundary_id, name, contact_type, geo_unit):
        self._boundary_id = boundary_id
        self._name = name
        self._contact_type = contact_type
        self._geo_unit = geo_unit

    _name: str
