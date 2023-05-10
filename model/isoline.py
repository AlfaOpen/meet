class Isoline:
    _isoline_id: int
    _filename: str
    _name: str
    _boundary_id: int
    _iso_type: str

    def get_isoline_id(self):  # PRIMARY KEY
        if self._isoline_id == 0:
            return "Not Present"
        return self._isoline_id

    def get_filename(self):
        return self._filename

    def set_filename(self, filename):
        self._filename = filename

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_boundary_id(self):  # FOREIGN KEY
        if self._boundary_id == 0:
            return "Not Present"
        return self._boundary_id

    def get_iso_type(self):
        return self._iso_type

    def set_iso_type(self, iso_type):
        self._iso_type = iso_type
