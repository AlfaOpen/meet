from model.geological_event import GeologicalEvent

class GeologicalEventMapper:

    def to_model(self, geological_event_dto):
        geological_event = GeologicalEvent()
        geological_event.set_era_id(geological_event_dto.get_era_id())
        geological_event.set_geo_unit(geological_event_dto.get_geo_unit())
        geological_event.set_older_named_age(geological_event_dto.get_older_named_age())
        geological_event.set_younger_named_age(geological_event_dto.get_younger_named_age())
