class IsolineInfo:
    _coordinate_id: int
    _isoline_id: int
    _iso_value: int

    def get_coordinate_id(self):  # PRIMARY KEY
        if self._coordinate_id == 0:
            return "Not Present"
        return self._coordinate_id

    def get_isoline_id(self):  # FOREIGN KEY
        if self._isoline_id == 0:
            return "Not Present"
        return self._isoline_id

    def set_iso_value(self, iso_value):
        self._iso_value = iso_value

    def get_iso_value(self):
        return self._iso_value


