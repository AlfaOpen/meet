from model.geological_event import GeologicalEvent

class GeologicalEventMapper:

    def to_model(self, geological_event_dto):
        geological_event = GeologicalEvent()
        geological_event.set_era_id(geological_event_dto.get_era_id())
        geological_event.set_geo_unit(geological_event_dto.get_geo_unit())
        geological_event.set_older_named_age(geological_event_dto.get_older_named_age())
        geological_event.set_younger_named_age(geological_event_dto.get_younger_named_age())
        return geological_event

    def to_model_list_geological_event(self, list_geological_event_dto: list):
        model_list = []
        for dto in list_geological_event_dto:
            model_list.append(self.to_model(dto))
        return model_list