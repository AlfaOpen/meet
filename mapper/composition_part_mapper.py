from model.composition_part import CompositionPart

class CompositionPartMapper:

    def to_model(self, composition_part_dto):
        composition_part = CompositionPart()
        composition_part.set_part_id(composition_part_dto.get_part_id())
        composition_part.set_geo_unit(composition_part_dto.get_geo_unit())
        composition_part.set_material(composition_part_dto.get_material())
        composition_part.set_role(composition_part_dto.get_role())
