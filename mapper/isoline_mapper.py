from model.isoline import Isoline


class IsolineMapper:
# dal mapper mi escono tanti modelli, ogni modello è un oggetto (quindi "una riga" con tutti gli attributi) --> mi
# escono tanti models quante sono "le righe"
    def to_model(self, isoline_dto):
        isoline = Isoline()
        isoline.set_isoline_id(isoline_dto.get_isoline_id())
        isoline.set_filename(isoline_dto.get_filename())
        isoline.set_name(isoline_dto.get_name())
        isoline.set_boundary_id(isoline_dto.get_boundary_id())
        isoline.set_iso_type(isoline_dto.get_iso_type())
        return isoline

    def to_model_list_isoline(self, list_isoline_dto: list):
        model_list = []
        for dto in list_isoline_dto:
            model_list.append(self.to_model(dto))
        return model_list
