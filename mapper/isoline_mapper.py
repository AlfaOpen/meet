from model.isoline import Isoline


class IsolineMapper:

    def to_model(self, isoline_dto):
        isoline = Isoline()
        isoline.set_isoline_id(isoline_dto.get_isoline_id())
        isoline.set_filename(isoline_dto.get_filename())
        isoline.set_name(isoline_dto.get_name())
        isoline.set_boundary_id(isoline_dto.get_boundary_id())
        isoline.set_iso_type(isoline_dto.get_iso_type())
