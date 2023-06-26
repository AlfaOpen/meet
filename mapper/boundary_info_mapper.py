from model.boundary_info import BoundaryInfo


class BoundaryInfoMapper:

    def to_model(self, boundary_info_dto):
        boundary_info = BoundaryInfo()
        boundary_info.set_id(boundary_info_dto.get_id())
        boundary_info.set_boundary_id(boundary_info_dto.get_boundary_id())
        boundary_info.set_x(boundary_info_dto.get_x())
        boundary_info.set_y(boundary_info_dto.get_y())
        boundary_info.set_depth(boundary_info_dto.get_depth())
        boundary_info.set_thickness(boundary_info_dto.get_thickness())
        boundary_info.set_geometry(boundary_info_dto.get_geometry())
        return boundary_info

    def to_model_list_boundary_info(self, list_boundary_info_dto: list):
        model_list = []
        for dto in list_boundary_info_dto:
            model_list.append(self.to_model(dto))
        return model_list
