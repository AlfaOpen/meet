from model.geologic_unit import GeologicUnit

class GeologicUnitMapper:

    def to_model(self,  geologic_unit_dto):
        geologic_unit = GeologicUnit()
        geologic_unit.set_geo_unit_id(geologic_unit_dto.get_geo_unit_id())
        geologic_unit.set_name(geologic_unit_dto.get_name())
        geologic_unit.set_description(geologic_unit_dto.get_description())
        geologic_unit.set_ref_geo_unit(geologic_unit_dto.get_ref_geo_unit())
        geologic_unit.set_geo_unit_type(geologic_unit_dto.get_geo_unit_type())
        return geologic_unit

    def to_model_list_geologic_unit(self, list_geo_dto: list):
        model_list = []
        for dto in list_geo_dto:
            model_list.append(self.to_model(dto))
            print(model_list)
        return model_list