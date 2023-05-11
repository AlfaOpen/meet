from model.isoline_info import IsolineInfo


class IsolineInfoMapper:

    def to_model(self, isoline_info_dto):
        isoline_info = IsolineInfo()
        isoline_info.set_coordinate_id(isoline_info_dto.get_coordinate_id())
        isoline_info.set_isoline_id(isoline_info_dto.get_isoline_id())
        isoline_info.set_iso_value(isoline_info_dto.get_iso_value())

