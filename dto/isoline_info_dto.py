class IsolineInfoDto:

    def __init__(self):
        self._id = None
        self._isoline_id = None
        self._iso_value = None
        self._x = None
        self._y = None
        self._isobata_id = None
        self._vertex_index = None
        self._vertex_part = None
        self._vertex_part_index = None
        self._distance = None
        self._angle = None

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

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y

    def set_isobata_id(self, isobata_id):
        self._isobata_id = isobata_id

    def get_isobata_id(self):
        return self._isobata_id

    def set_vertex_index(self, vertex_index):
        self._vertex_index = vertex_index

    def get_vertex_index(self):
        return self._vertex_index

    def set_vertex_part(self, vertex_part):
        self._vertex_part = vertex_part

    def get_vertex_part(self):
        return self._vertex_part

    def set_vertex_part_index(self, vertex_part_index):
        self._vertex_part_index = vertex_part_index

    def get_vertex_part_index(self):
        return self._vertex_part_index

    def set_distance(self, distance):
        self._distance = distance

    def get_distance(self):
        return self._distance

    def set_angle(self, angle):
        self._angle = angle

    def get_angle(self):
        return self._angle
