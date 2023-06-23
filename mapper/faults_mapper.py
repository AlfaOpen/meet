from model.faults import Faults


class FaultsMapper:

    def to_model(self, faults_dto):
        faults = Faults()
        faults.set_id(faults_dto.get_id())
        faults.set_dip_angle(faults_dto.get_dip_angle())
        faults.set_dip_direct(faults_dto.get_dip_direct())
        faults.set_eval_meth(faults_dto.get_eval_meth())
        faults.set_observe_meth(faults_dto.get_observe_meth())
        faults.set_fid(faults_dto.get_fid())
        faults.set_fault_sys(faults_dto.get_fault_sys())
        faults.set_fault_type(faults_dto.get_fault_type())
        faults.set_length(faults_dto.get_length())
        faults.set_local_name(faults_dto.get_local_name())
        faults.set_mean_dip(faults_dto.get_mean_dip())
        faults.set_mean_dip_azi(faults_dto.get_mean_dip_azi())
        faults.set_mean_strike(faults_dto.get_mean_strike())
        faults.set_young_unit(faults_dto.get_young_unit())
        faults.set_old_unit(faults_dto.get_old_unit())
        faults.set_ref_type(faults_dto.get_ref_type())
        faults.set_reference(faults_dto.get_reference())
        faults.set_strike(faults_dto.get_strike())
        faults.set_uri(faults_dto.get_uri())

        return faults

    def to_model_list_faults(self, list_faults_dto: list):
        model_list = []
        for dto in list_faults_dto:
            model_list.append(self.to_model(dto))
        return model_list
