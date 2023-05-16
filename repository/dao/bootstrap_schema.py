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
