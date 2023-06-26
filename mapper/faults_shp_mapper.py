from model.faults_shp import FaultsShp


class FaultsShpMapper:

    def to_model(self, faults_shp_dto):
        faults_shp = FaultsShp()
        faults_shp.set_id(faults_shp_dto.get_id())
        faults_shp.set_fault_id(faults_shp_dto.get_fault_id())
        faults_shp.set_x(faults_shp_dto.get_x())
        faults_shp.set_y(faults_shp_dto.get_y())
        faults_shp.set_local_name(faults_shp_dto.get_local_name())
        faults_shp.set_vertex_index(faults_shp_dto.get_vertex_index())
        faults_shp.set_vertex_part(faults_shp_dto.get_vertex_part())
        faults_shp.set_vertex_part_index(faults_shp_dto.get_vertex_part_index())
        faults_shp.set_distance(faults_shp_dto.get_distance())
        faults_shp.set_angle(faults_shp_dto.get_angle())
        faults_shp.set_geometry(faults_shp_dto.get_geometry())

        return faults_shp

    def to_model_list_faults_shp(self, list_faults_shp_dto: list):
        model_list = []
        for dto in list_faults_shp_dto:
            model_list.append(self.to_model(dto))
        return model_list
