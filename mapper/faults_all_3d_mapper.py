from model.faults_all_3d import FaultsAll3d


class FaultsAll3dMapper:

    def to_model(self, faults_all_3d_dto):
        faults_all_3d = FaultsAll3d()
        faults_all_3d.set_id(faults_all_3d_dto.get_id())
        faults_all_3d.set_fault_id(faults_all_3d_dto.get_fault_id())
        faults_all_3d.set_x(faults_all_3d_dto.get_x())
        faults_all_3d.set_y(faults_all_3d_dto.get_y())
        faults_all_3d.set_depth(faults_all_3d_dto.get_depth())
        faults_all_3d.set_local_name(faults_all_3d_dto.get_local_name())
        return faults_all_3d

    def to_model_list_faults_all_3d(self, list_faults_all_3d_dto: list):
        model_list = []
        for dto in list_faults_all_3d_dto:
            model_list.append(self.to_model(dto))
        return model_list
