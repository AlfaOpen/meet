class BoundaryDto:
    def __init__(self, info_3d_id, boundary_id, x, y, depth, thickness):
        self._info_3d_id = info_3d_id
        self._boundary_id = boundary_id
        self._x = x
        self._y = y
        self._depth = depth
        self._thickness = thickness