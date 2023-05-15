class GeologicalEvent:

    def __init__(self):
        self._era_id = None
        self._geo_unit = None
        self._older_named_age = None
        self._younger_named_age = None

    def get_era_id(self):  # PRIMARY KEY
        if self._era_id is None:
            return "Not Present"
        return self._era_id

    def set_era_id(self, era_id):
        self._era_id = era_id

    def get_geo_unit(self):  # FOREIGN KEY
        if self._geo_unit == 0:
            return "Not Present"
        return self._geo_unit

    def set_geo_unit(self, geo_unit):
        self._geo_unit = geo_unit

    def get_older_named_age(self):
        return self._older_named_age

    def set_older_named_age(self, older_named_age):
        self._older_named_age = older_named_age

    def get_younger_named_age(self):
        return self._younger_named_age

    def set_younger_named_age(self, younger_named_age):
        self._younger_named_age = younger_named_age
