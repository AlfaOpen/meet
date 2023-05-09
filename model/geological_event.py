class GeologicalEvent:
    _era_id: int
    _geo_unit: int
    _older_named_age: str
    _younger_named_age: str

    def get_era_id(self):
        if self._era_id == 0:
            return "Not Present"
        return self._era_id

    def get_geo_unit(self):
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

