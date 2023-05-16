class IsolineInfoDto:

    def __init__(self):
        self._id = None
        self._isoline_id = None
        self._iso_value = None

    def get_id(self):  # PRIMARY KEY
        return self._id

    def set_id(self, coordinate_id):
        self._id = coordinate_id

    def get_isoline_id(self):  # FOREIGN KEY
        return self._isoline_id

    def set_isoline_id(self, isoline_id):
        self._isoline_id = isoline_id

    def set_iso_value(self, iso_value):
        self._iso_value = iso_value

    def get_iso_value(self):
        return self._iso_value
