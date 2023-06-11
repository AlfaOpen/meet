from model.boundary import Boundary

class BoundaryMapper:

    def to_model(self, boundary_dto):
        boundary = Boundary()
        boundary.set_boundary_id(boundary_dto.get_boundary_id())
        boundary.set_name(boundary_dto.get_name())
        boundary.set_contact_type(boundary_dto.get_contact_type())
        boundary.set_geo_unit(boundary_dto.get_geo_unit())
        return boundary

    def to_model_list_boundary(self, list_boundary_dto: list):
        model_list = []
        for dto in list_boundary_dto:
            model_list.append(self.to_model(dto))
        return model_list

