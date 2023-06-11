class FaultsAll3dDto:

    def __init__(self):
        self._id = None
        self._fault_id = None
        self._x = None
        self._y = None
        self._depth = None
        self._local_name = None

    def get_id(self):  # PRIMARY KEY
        return self._id

    def set_id(self, info_3d_id):
        self._id = info_3d_id

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

    def set_depth(self, depth):
        self._depth = depth

    def get_depth(self):
        return self._depth

    def set_local_name(self, local_name):
        self._local_name = local_name

    def get_local_name(self):
        return self._local_name