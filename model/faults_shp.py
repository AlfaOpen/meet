class FaultsShp:

    def __init__(self):
        self._id = None
        self._fault_id = None
        self._x = None
        self._y = None
        self._local_name = None
        self._vertex_index = None
        self._vertex_part = None
        self._vertex_part_index = None
        self._distance = None
        self._angle = None

    def get_id(self):  # PRIMARY KEY
        return self._id

    def set_id(self, coordinate_id):
        self._id = coordinate_id

    def get_fault_id(self):  # FOREIGN KEY
        return self._fault_id

    def set_fault_id(self, fault_id):
        self._fault_id = fault_id

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y

    def set_local_name(self, local_name):
        self._local_name = local_name

    def get_local_name(self):
        return self._local_name

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
