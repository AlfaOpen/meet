class BoundaryInfo:

    def __init__(self):
        self._id = None
        self._boundary_id = None
        self._x = None
        self._y = None
        self._depth = None
        self._thickness = None
        self._geometry = None

    def get_id(self):  # PRIMARY KEY
        return self._id

    def set_id(self, info_3d_id):
        self._id = info_3d_id

    def get_boundary_id(self):  # FOREIGN KEY
        return self._boundary_id

    def set_boundary_id(self, boundary_id):
        self._boundary_id = boundary_id

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y

    def set_depth(self, depth):
        self._depth = depth

    def get_depth(self):
        return self._depth

    def set_thickness(self, thickness):
        self._thickness = thickness

    def get_thickness(self):
        return self._thickness

    def set_geometry(self, geometry):
        self._geometry = geometry

    def get_geometry(self):
        return self._geometry
