from model.faults import Faults


def model_to_tuple_faults(model: Faults):
    return (str(model.get_id()),
            model.get_dip_angle(),
            model.get_dip_direct(),
            model.get_eval_meth(),
            model.get_observe_meth(),
            str(model.get_fid()),
            model.get_fault_sys(),
            model.get_fault_type(),
            str(model.get_length()),
            model.get_local_name(),
            str(model.get_mean_dip()),
            str(model.get_mean_dip_azi()),
            str(model.get_mean_strike()),
            model.get_young_unit(),
            model.get_old_unit(),
            model.get_ref_type(),
            model.get_reference(),
            model.get_strike(),
            model.get_uri(),
            str(model.get_geometry()))


class FaultsRepo:
    insert_query = """ INSERT INTO "Faults"  (
   "id",
    "dipAngle",
    "dipDirect",
    "evalMeth" ,
    "observMeth" ,
    "fid",
    "faultSys",
    "faultType",
    "length",
    "localName",
    "meanDip",
    "meanDipAzi",
    "meanStrike",
    "youngUnit" ,
    "oldUnit",
    "refType",
    "reference",
    "strike",
    "uri",
     "geometry") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    def __init__(self, connection):
        self.connection = connection

    def populate_faults(self, models):
        cursor = self.connection.cursor()
        for i in models:
            values = model_to_tuple_faults(i)
            cursor.execute(self.insert_query, values)
        self.connection.commit()
