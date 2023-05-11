from model.boundary import Boundary


class BoundaryMapper:

    def to_model(self, boundary_dto):
        boundary = Boundary()
        boundary.set_name(boundary_dto.get_name())

