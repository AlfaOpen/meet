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
    "idGeoUnit" integer NOT NULL,
    "name" "char",
    "description" "char",
    refGeoUnit "char",
    "geologicUnitType" "char",
    CONSTRAINT "GeologicUnit_pkey" PRIMARY KEY ("idGeoUnit")
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."GeologicUnit"
    OWNER to giulia;'''

    return table_geologic_unit


def boundary():
    table_boundary = '''CREATE TABLE IF NOT EXISTS public."Boundary"
    (
    "idBoundary" INT NOT NULL,
    "name" "char",
    "contactType" "char",
    geoUnit INT,
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
    "x" numeric,
    "y" numeric,
    "depth" numeric,
    "thickness" numeric,
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
    geoUnit integer,
    "Material" "char",
    "Role" "char",
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
    geoUnit integer,
    "olderNamedAge" "char",
    "YoungerNamedAge" "char",
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
    "idIsoline" integer NOT NULL,
    "Filename" varchar,
    "name" varchar,
    "BoundaryId" integer,
    "isoType" varchar,
    CONSTRAINT "Isoline_pkey" PRIMARY KEY ("idIsoline"),
    CONSTRAINT "Isoline_Boundaryid_fkey" FOREIGN KEY ("BoundaryId")
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
    "idCoordinate" integer NOT NULL,
    "Isoline" integer,
    "isoValue" numeric,
    CONSTRAINT "IsolineInfo_pkey" PRIMARY KEY ("idCoordinate"),
    CONSTRAINT "IsolineInfo_Isoline_fkey" FOREIGN KEY ("Isoline")
        REFERENCES public."Isoline" ("idIsoline") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."IsolineInfo"
        OWNER to giulia;'''

    return table_isoline_info
