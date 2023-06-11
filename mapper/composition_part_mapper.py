from model.composition_part import CompositionPart

class CompositionPartMapper:

    def to_model(self, composition_part_dto):
        composition_part = CompositionPart()
        composition_part.set_part_id(composition_part_dto.get_part_id())
        composition_part.set_geo_unit(composition_part_dto.get_geo_unit())
        composition_part.set_lithology_value1(composition_part_dto.get_lithology_value1())
        composition_part.set_lithology_value2(composition_part_dto.get_lithology_value2())
        composition_part.set_composition_part_role_value1(composition_part_dto.get_composition_part_role_value1())
        composition_part.set_composition_part_role_value2(composition_part_dto.get_composition_part_role_value2())
        return composition_part

    def to_model_list_composition_part(self, list_composition_part_dto: list):
        model_list = []
        for dto in list_composition_part_dto:
            model_list.append(self.to_model(dto))
        return model_list
