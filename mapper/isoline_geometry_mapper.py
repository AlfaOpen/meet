from model.isoline_geometry import IsolineGeometry


class IsolineGeometryMapper:

    def to_model(self, isoline_geometry_dto):
        isoline_geometry = IsolineGeometry()
        isoline_geometry.set_id(isoline_geometry_dto.get_id())
        isoline_geometry.set_isobata_id(isoline_geometry_dto.get_isobata_id())
        isoline_geometry.set_isoline_id(isoline_geometry_dto.get_isoline_id())
        isoline_geometry.set_geometry(isoline_geometry_dto.get_geometry())

        return isoline_geometry

    def to_model_list_isoline_geometry(self, list_isoline_geometry_dto: list):
        model_list = []
        for dto in list_isoline_geometry_dto:
            model_list.append(self.to_model(dto))
        return model_list
