from model.boundary_info import BoundaryInfo


class BoundaryInfoMapper:

    def to_model(self, boundary_info_dto):
        boundary_info = BoundaryInfo()
        boundary_info.set_info_3d_id(boundary_info_dto.get_info_3d_id())
        boundary_info.set_boundary_id(boundary_info_dto.get_boundary_id())
        boundary_info.set_x(boundary_info_dto.get_x())
        boundary_info.set_y(boundary_info_dto.get_y())
        boundary_info.set_depth(boundary_info_dto.get_depth())
        boundary_info.set_thickness(boundary_info_dto.get_thickness())
