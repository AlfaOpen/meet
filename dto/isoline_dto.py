class IsolineDto:

    def __init__(self):
        self._isoline_id = None
        self._filename = None
        self._name = None
        self._boundary_id = None
        self._iso_type = None

    def get_isoline_id(self):  # PRIMARY KEY
        return self._isoline_id

    def set_isoline_id(self, isoline_id):
        self._isoline_id = isoline_id

    def get_filename(self):
        return self._filename

    def set_filename(self, filename):
        self._filename = filename

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_boundary_id(self):  # FOREIGN KEY
        return self._boundary_id

    def set_boundary_id(self, boundary_id):
        self._boundary_id = boundary_id

    def get_iso_type(self):
        return self._iso_type

    def set_iso_type(self, iso_type):
        self._iso_type = iso_type
