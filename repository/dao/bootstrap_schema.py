import os

from service.dynamic_load_service import DynamicLoad
from utility.parser import parse_method_name


class BoostrapSchema:
    """Docstring della classe.
    
    In Boostrap Schema è definito l'attributo "table_list", una lista appunto contenente delle funzioni, 
     ognuna delle quali contiene la query per la creazione della relativa tabella.
     """

    def __init__(self):
        self.table_list = [geologic_unit(), boundary(), boundary_info(),
                           isoline(), isoline_info(), composition_part(),
                           geological_event(), faults(), faults_shp(), faults_all_3d(), procedure()]

    def execute_query(self, connection):
        cursor = connection.cursor()
        for i in self.table_list:
            cursor.execute(i)

    def commit_query(self, connection):
        for i in self.table_list:
            connection.commit()
        print("Table created successfully in PostgresSQL ")


def geologic_unit():
    table_geologic_unit = '''CREATE TABLE IF NOT EXISTS public."GeologicUnit"
    (
    "inspireId" varchar NOT NULL,
    "name" varchar,
    "description" varchar,
    "refGeoUnit" varchar,
    "geologicUnitType" varchar,
    CONSTRAINT "GeologicUnit_pkey" PRIMARY KEY ("inspireId")
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
        REFERENCES public."GeologicUnit" ("inspireId") MATCH SIMPLE
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
        REFERENCES public."GeologicUnit" ("inspireId") MATCH SIMPLE
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
        REFERENCES public."GeologicUnit" ("inspireId") MATCH SIMPLE
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
    "x" float,
    "y" float,
    "idIsobata" integer,
    "vertexIndex" integer,
    "vertexPart" integer,
    "vertexPartIndex" integer,
    "distance" float,
    "angle" float,
    
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


def faults():
    table_faults = '''CREATE TABLE IF NOT EXISTS public."Faults"
    (
    "id" varchar NOT NULL,
    "dipAngle" varchar,
    "dipDirect" varchar,
    "evalMeth"  varchar,
    "observMeth" varchar,
    "fid" int8 unique ,
    "faultSys" varchar,
    "faultType" varchar,
    "length" integer,
    "localName" varchar,
    "meanDip" integer,
    "meanDipAzi" integer,
    "meanStrike" integer,
    "youngUnit"  varchar,
    "oldUnit" varchar,
    "refType" varchar,
    "reference" varchar,
    "strike" varchar,
    "uri" varchar,
    
    CONSTRAINT "Faults._pkey" PRIMARY KEY ("id")
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."Faults"
        OWNER to giulia;'''

    return table_faults


def faults_shp():
    table_faults_shp = '''CREATE TABLE IF NOT EXISTS public."FaultsShp"
    (
    "id" integer NOT NULL,
    "faultId" int8,
    "x" float,
    "y" float,
    "localName" varchar,
    "vertexIndex" text,
    "vertexPart" text,
    "vertexPartIndex" text,
    "distance" text,
    "angle" text,

    CONSTRAINT "FaultsShp_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "FaultsShp_Faults_fkey" FOREIGN KEY ("faultId")
        REFERENCES public."Faults" ("fid") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."FaultsShp"
        OWNER to giulia;'''

    return table_faults_shp


def faults_all_3d():
    table_faults_all_3d = '''CREATE TABLE IF NOT EXISTS public."FaultsAll3d"
    (
    "id" integer NOT NULL,
    "faultId" int8, 
    "x" float,
    "y" float,
    "depth" float,
    "localName" varchar,

    CONSTRAINT "FaultsAll3d_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "FaultsAll3d_Faults_fkey" FOREIGN KEY ("faultId")
        REFERENCES public."Faults" ("fid") MATCH SIMPLE 
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    )
    TABLESPACE pg_default;
    ALTER TABLE IF EXISTS public."FaultsAll3d"
        OWNER to giulia;'''

    return table_faults_all_3d


def procedure():
    table_procedure = '''CREATE TABLE IF NOT EXISTS public."Procedure"
        (
        "id" int NOT NULL, 
        "nome" varchar UNIQUE,
        "listaFileExcel" text[],
        "listaPath" text[], 
        "listaColonne" text[],

        CONSTRAINT "Procedure_pkey" PRIMARY KEY ("id")
        )
        TABLESPACE pg_default;
        ALTER TABLE IF EXISTS public."Procedure"
            OWNER to giulia;'''

    return table_procedure


# def mapper_cycle scorre gli excel, si fa da solo i dto dall'excel, dal nome del dto si fa il mapper e per ogni
# uscita del mapper fa da solo il repository con le insert

def mapper_cycle(connection, lista_colonne):
    """ Definizione della funzione mappercycle.

    """
    excel_list = os.listdir(
        r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\dati_geologici_database")
    dynamic_load = DynamicLoad()
    for i in range(0, len(excel_list)):
        item = excel_list[i]
        if item == "GeologicUnit.xlsx":
            excel_list.insert(0, excel_list.pop(i))
            break
    for i in range(0, len(excel_list)):
        file = excel_list[i]
        path = "C:\\Users\\giuli\\OneDrive\\Desktop\\Progetto ISPRA\\Test_Dataset_PoBasin\\dati_geologici_database\\" + file
        lista_num_col = lista_colonne[i]
        # decommentare sotto se si vuole chiedere in input il numero di colonne
        # lista_num_col = []
        # input_col = input(
        #     "Selezionare le colonne di " + file + ":\n Inserire 'all' se si vogliono tutte le colonne, oppure una "
        #                                           "lista con gli indici delle relative colonne\n")
        # if input_col != 'all':
        #     ind_list = ast.literal_eval(input_col)
        #     lista_num_col = ind_list
        model_class_str = file[0:-5]
        file_dto = (model_class_str + "Dto")
        tabled = dynamic_load.to_dto(path, file_dto, lista_num_col)
        file_mapper = globals()[model_class_str + "Mapper"]()
        str_par1 = parse_method_name(model_class_str)
        metodo_par1 = "to_model_list_" + str_par1
        metodo1 = getattr(file_mapper, metodo_par1)
        models_list = metodo1(tabled)
        file_repo = globals()[model_class_str + "Repo"](connection)
        metodo_par2 = "populate_" + str_par1
        metodo2 = getattr(file_repo, metodo_par2)
        metodo2(models_list)
    print('Insert effettuate correttamente')


def clear_schema_all(connection):
    drop_query = '''DROP TABLE if exists public."CompositionPart", public."GeologicalEvent", public."IsolineInfo",
     public."Isoline", public."BoundaryInfo", public."Boundary", public."GeologicUnit", public."Faults", public."FaultsShp", public."FaultsAll3d" '''
    cursor = connection.cursor()
    cursor.execute(drop_query)
    connection.commit()
    print('Tutte le tabelle sono state eliminate')


def clear_schema_geounit(connection):
    drop_query = '''DROP TABLE if exists public."CompositionPart", public."GeologicalEvent", public."IsolineInfo",
     public."Isoline", public."BoundaryInfo", public."Boundary", public."GeologicUnit" '''
    cursor = connection.cursor()
    cursor.execute(drop_query)
    connection.commit()
    print('Le tabelle selezionate sono state eliminate')


def clear_schema_faults(connection):
    drop_query = '''DROP TABLE if exists public."Faults", public."FaultsShp", public."FaultsAll3d" '''
    cursor = connection.cursor()
    cursor.execute(drop_query)
    connection.commit()
    print('Le tabelle selezionate sono state eliminate')

def remake_schema_procedure(connection):
    drop_query = '''DROP TABLE if exists public."Procedure" '''
    cursor = connection.cursor()
    cursor.execute(drop_query)
    cursor.execute(procedure())
    connection.commit()
    print('La tabella procedura è stata eliminata e nuovamente creata')

# public."CompositionPart", public."GeologicalEvent", public."IsolineInfo",
#     public."Isoline", public."BoundaryInfo", public."Boundary", public."GeologicUnit"
#  public."Faults", public."FaultsShp", public."FaultsAll3d"
