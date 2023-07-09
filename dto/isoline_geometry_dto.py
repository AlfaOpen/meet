class IsolineGeometryDto:

    def __init__(self):
        self._id = None
        self._isoline_id = None
        self._isobata_id = None
        self._geometry = None

    def get_id(self):  # PRIMARY KEY
        return self._id

    def set_id(self, coordinate_id):
        self._id = coordinate_id

    def get_isoline_id(self):  # PRIMARY KEY
        return self._isoline_id

    def set_isoline_id(self, isoline_id):
        self._isoline_id = isoline_id

    def set_isobata_id(self, isobata_id):
        self._isobata_id = isobata_id

    def get_isobata_id(self):
        return self._isobata_id

    def set_geometry(self, geometry):
        self._geometry = geometry

    def get_geometry(self):
        return self._geometry