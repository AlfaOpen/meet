class FaultsDto:

    def __init__(self):
        self._id = None
        self._dip_angle = None
        self._dip_direct = None
        self._eval_meth = None
        self._observe_meth = None
        self._fid = None
        self._fault_sys = None
        self._fault_type = None
        self._length = None
        self._local_name = None
        self._mean_dip = None
        self._mean_dip_azi = None
        self._mean_strike = None
        self._young_unit = None
        self._old_unit = None
        self._ref_type = None
        self._reference = None
        self._strike = None
        self._uri = None

    def get_id(self):  # PRIMARY KEY
        return self._id

    def set_id(self, id):
        self._id = id

    def get_dip_angle(self):
        return self._dip_angle

    def set_dip_angle(self, dip_angle):
        self._dip_angle = dip_angle

    def get_dip_direct(self):
        return self._dip_direct

    def set_dip_direct(self, dip_direct):
        self._dip_direct = dip_direct

    def set_eval_meth(self, eval_meth):
        self._eval_meth = eval_meth

    def get_eval_meth(self):
        return self._eval_meth

    def set_observe_meth(self, observe_meth):
        self._observe_meth = observe_meth

    def get_observe_meth(self):
        return self._observe_meth

    def set_fid(self, fid):
        self._fid = fid

    def get_fid(self):
        return self._fid

    def set_fault_sys(self, fault_sys):
        self._fault_sys = fault_sys

    def get_fault_sys(self):
        return self._fault_sys

    def set_fault_type(self, fault_type):
        self._fault_type = fault_type

    def get_fault_type(self):
        return self._fault_type

    def set_length(self, length):
        self._length = length

    def get_length(self):
        return self._length

    def set_local_name(self, local_name):
        self._local_name = local_name

    def get_local_name(self):
        return self._local_name

    def set_mean_dip(self, mean_dip):
        self._mean_dip = mean_dip

    def get_mean_dip(self):
        return self._mean_dip

    def set_mean_dip_azi(self, mean_dip_azi):
        self._mean_dip_azi = mean_dip_azi

    def get_mean_dip_azi(self):
        return self._mean_dip_azi

    def set_mean_strike(self, mean_strike):
        self._mean_strike = mean_strike

    def get_mean_strike(self):
        return self._mean_strike

    def set_young_unit(self, young_unit):
        self._young_unit = young_unit

    def get_young_unit(self):
        return self._young_unit

    def set_old_unit(self, old_unit):
        self._old_unit = old_unit

    def get_old_unit(self):
        return self._old_unit

    def set_ref_type(self, ref_type):
        self._ref_type = ref_type

    def get_ref_type(self):
        return self._ref_type

    def set_reference(self, reference):
        self._reference = reference

    def get_reference(self):
        return self._reference

    def set_strike(self, strike):
        self._strike = strike

    def get_strike(self):
        return self._strike

    def set_uri(self, uri):
        self._uri = uri

    def get_uri(self):
        return self._uri
