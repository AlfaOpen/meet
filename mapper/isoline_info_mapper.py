from model.isoline_info import IsolineInfo


class IsolineInfoMapper:

    def to_model(self, isoline_info_dto):
        isoline_info = IsolineInfo()
        isoline_info.set_id(isoline_info_dto.get_id())
        isoline_info.set_isoline_id(isoline_info_dto.get_isoline_id())
        isoline_info.set_iso_value(isoline_info_dto.get_iso_value())
        return isoline_info

    def to_model_list_iso_info(self, list_isoline_info_dto: list):
        model_list = []
        for dto in list_isoline_info_dto:
            model_list.append(self.to_model(dto))
        return model_list

