class IsolineInfo:

    def __init__(self):
        self._coordinate_id = None
        self._isoline_id = None
        self._iso_value = None

    def get_coordinate_id(self):  # PRIMARY KEY
        if self._coordinate_id == 0:
            return "Not Present"
        return self._coordinate_id

    def set_coordinate_id(self, coordinate_id):
        self._coordinate_id = coordinate_id

    def get_isoline_id(self):  # FOREIGN KEY
        if self._isoline_id == 0:
            return "Not Present"
        return self._isoline_id

    def set_isoline_id(self, isoline_id):
        self._isoline_id = isoline_id

    def set_iso_value(self, iso_value):
        self._iso_value = iso_value

    def get_iso_value(self):
        return self._iso_value


