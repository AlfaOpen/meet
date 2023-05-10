class BoundaryInfo:
    _info_3D_id: int
    _boundary_id: int
    _x: int
    _y: int
    _depth: int
    _thickness: int

    def get_info_3d_id(self):  # PRIMARY KEY
        if self._info_3D_id == 0:
            return "Not Present"
        return self._info_3D_id

    def get_boundary_id(self):  # FOREIGN KEY
        if self._boundary_id == 0:
            return "Not Present"
        return self._boundary_id

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

