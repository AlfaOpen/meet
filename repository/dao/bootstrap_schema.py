from dto.isoline_info_dto import IsolineInfoDto
from mapper.isoline_info_mapper import IsolineInfoMapper
from mapper.isoline_mapper import IsolineMapper
from model.isoline import Isoline
from model.isoline_info import IsolineInfo
from repository.dao.isoline_info_repository import IsolineInfoRepo
from repository.dao.isoline_repository import IsolineRepo
from repository.dynamic_load.dynamic_load import DynamicLoad
from utility.parser import parse_method_name
from dto.isoline_dto import IsolineDto
from dto.boundary_dto import BoundaryDto
from dto.boundary_info_dto import BoundaryInfoDto
from dto.composition_part_dto import CompositionPartDto
from dto.geologic_unit_dto import GeologicUnitDto
from dto.geological_event_dto import GeologicalEventDto
from mapper.boundary_info_mapper import BoundaryInfoMapper
from mapper.boundary_mapper import BoundaryMapper
from mapper.composition_part_mapper import CompositionPartMapper
from mapper.geologic_unit_mapper import GeologicUnitMapper
from mapper.geological_event_mapper import GeologicalEventMapper
from repository.dao.boundary_info_repository import BoundaryInfoRepo
from repository.dao.boundary_repository import BoundaryRepo
from repository.dao.composition_part_repository import CompositionPartRepo
from repository.dao.geologic_unit_repository import GeologicUnitRepo
from repository.dao.geological_event_repository import GeologicalEventRepo


class BoostrapSchema:

    def __init__(self):
        self.table_list = [geologic_unit(), boundary(), boundary_info(),
                           isoline(), isoline_info(), composition_part(),
                           geological_event()]

    def execute_query(self, connection):
        cursor = connection.cursor()
        for i in self.table_list:
            cursor.execute(i)

    def commit_query(self, connection):
        for i in self.table_list:
            connection.commit()


def geologic_unit():
    table_geologic_unit = '''CREATE TABLE IF NOT EXISTS public."GeologicUnit"
    (
    "idGeoUnit" varchar NOT NULL,
    "name" varchar,
    "description" varchar,
    "refGeoUnit" varchar,
    "geologicUnitType" varchar,
    CONSTRAINT "GeologicUnit_pkey" PRIMARY KEY ("idGeoUnit")
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."GeologicUnit"
    OWNER to giulia;'''

    return table_geologic_unit


def boundary():
    table_boundary = '''CREATE TABLE IF NOT EXISTS public."Boundary"
    (
    "idBoundary" integer NOT NULL,
    "name" varchar,
    "contactType" varchar,
    geoUnit varchar,
    CONSTRAINT "Boundary_pkey" PRIMARY KEY ("idBoundary"),
    CONSTRAINT geoUnit FOREIGN KEY (geoUnit)
        REFERENCES public."GeologicUnit" ("idGeoUnit") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."Boundary"
        OWNER to giulia;'''

    return table_boundary


def boundary_info():
    table_boundary_info = '''CREATE TABLE IF NOT EXISTS public."BoundaryInfo"
    (
    "idInfo3D" integer NOT NULL,
    "boundaryId" integer,
    "x" float,
    "y" float,
    "depth" float,
    "thickness" float,
    CONSTRAINT "BoundaryInfo_pkey" PRIMARY KEY ("idInfo3D"),
    CONSTRAINT "BoundaryInfo_Boundaryid_fkey" FOREIGN KEY ("boundaryId")
        REFERENCES public."Boundary" ("idBoundary") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."BoundaryInfo"
        OWNER to giulia;'''

    return table_boundary_info


def composition_part():
    table_composition_part = '''CREATE TABLE IF NOT EXISTS public."CompositionPart"
    (
    "idPart" integer NOT NULL,
    geoUnit varchar,
    "Material1" varchar,
    "Material2" varchar,
    "Role1" varchar,
    "Role2" varchar,
    CONSTRAINT "CompositionPart_pkey" PRIMARY KEY ("idPart"),
    CONSTRAINT "CompositionPart_geoUnit_fkey" FOREIGN KEY (geoUnit)
        REFERENCES public."GeologicUnit" ("idGeoUnit") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."CompositionPart"
        OWNER to giulia;'''

    return table_composition_part


def geological_event():
    table_geological_event = '''CREATE TABLE IF NOT EXISTS public."GeologicalEvent"
    (
    "idEra" integer NOT NULL,
    geoUnit varchar,
    "olderNamedAge" varchar,
    "YoungerNamedAge" varchar,
    CONSTRAINT "GeologicalEvent_pkey" PRIMARY KEY ("idEra"),
    CONSTRAINT "GeologicalEvent_geoUnit_fkey" FOREIGN KEY (geoUnit)
        REFERENCES public."GeologicUnit" ("idGeoUnit") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."GeologicalEvent"
        OWNER to giulia;'''

    return table_geological_event


def isoline():
    table_isoline = '''CREATE TABLE IF NOT EXISTS public."Isoline"
    (
    "idIsoline" varchar NOT NULL,
    "filename" varchar,
    "name" varchar,
    "boundaryId" integer,
    "isoType" varchar,
    CONSTRAINT "Isoline_pkey" PRIMARY KEY ("idIsoline"),
    CONSTRAINT "Isoline_Boundaryid_fkey" FOREIGN KEY ("boundaryId")
        REFERENCES public."Boundary" ("idBoundary") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."Isoline"
        OWNER to giulia;'''

    return table_isoline


def isoline_info():
    table_isoline_info = '''CREATE TABLE IF NOT EXISTS public."IsolineInfo"
    (
    "id" integer NOT NULL,
    isoline varchar,
    "isoValue" integer,
    CONSTRAINT "IsolineInfo_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "IsolineInfo_Isoline_fkey" FOREIGN KEY ("isoline")
        REFERENCES public."Isoline" ("idIsoline") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."IsolineInfo"
        OWNER to giulia;'''

    return table_isoline_info


# def mapper_cycle scorre gli excel, si fa da solo i dto dall'excel, dal nome del dto si fa il mapper e per ogni 
# uscita del mapper fa da solo il repository con le insert

def mapper_cycle(excel_list, path, num_col, model_class_str, connection):
    file_dto = (model_class_str + "Dto")
    dynamic_load = DynamicLoad()
    tabled = dynamic_load.to_dto(path, file_dto, num_col)
    file_mapper = globals()[model_class_str + "Mapper"]()
    str_par1 = parse_method_name(model_class_str)
    metodo_par1 = "to_model_list_" + str_par1
    metodo1 = getattr(file_mapper, metodo_par1)
    models_list = metodo1(tabled)
    file_repo = globals()[model_class_str + "Repo"](connection)
    metodo_par2 = "populate_" + str_par1
    metodo2 = getattr(file_repo, metodo_par2)
    metodo2(models_list)

    
