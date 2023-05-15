class BoundaryInfoDto:
    def __init__(self):
        self.info_3d_id = None
        self.boundary_id = None
        self.x = None
        self.y = None
        self.depth = None
        self.thickness = None

    def get_id(self):  # PRIMARY KEY
        if self.info_3d_id == 0:
            return "Not Present"
        return self.info_3d_id

    def set_id(self, info_3d_id):
        self.info_3d_id = info_3d_id

    def get_boundary_id(self):  # FOREIGN KEY
        if self.boundary_id == 0:
            return "Not Present"
        return self.boundary_id

    def set_boundary_id(self, boundary_id):
        self.boundary_id = boundary_id

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def set_depth(self, depth):
        self.depth = depth

    def get_depth(self):
        return self.depth

    def set_thickness(self, thickness):
        self.thickness = thickness

    def get_thickness(self):
        return self.thickness


