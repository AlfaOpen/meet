from model.boundary import Boundary


class BoundaryMapper:

    def to_model(self, boundary_dto):
        boundary = Boundary()
        boundary.set_name(boundary_dto.get_name())
        boundary.set_contact_type(boundary_dto.get_contact_type())
        boundary.set_geo_unit(boundary_dto.get_geo_unit())



