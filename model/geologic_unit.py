class GeologicUnit:

    def __init__(self):
        self._geo_unit_id = None
        self._name = None
        self._description = None
        self._ref_geo_unit = None
        self._geo_unit_type = None

    def get_geo_unit_id(self):  # PRIMARY KEY
        if self._geo_unit_id == 0:
            return "Not Present"
        return self._geo_unit_id

    def set_geo_unit_id(self, geo_unit_id):
        self._geo_unit_id = geo_unit_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_ref_geo_unit(self):
        return self._ref_geo_unit

    def set_ref_geo_unit(self, ref_geo_unit):
        self._ref_geo_unit = ref_geo_unit

    def get_geo_unit_type(self):
        return self._geo_unit_type

    def set_geo_unit_type(self, geo_unit_type):
        self._geo_unit_type = geo_unit_type




