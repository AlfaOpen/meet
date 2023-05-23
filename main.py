import logging

from mapper.isoline_info_mapper import IsolineInfoMapper
from model.boundary import Boundary
from repository.connection.connection import Connection, close_connection
from repository.dao.bootstrap_schema import clear_schema, BoostrapSchema, mapper_cycle
from repository.dao.isoline_info_repository import IsolineInfoRepo
from repository.dynamic_load.dynamic_load import DynamicLoad
from repository.reader.csv_reader import CSVReader
from utility.format_convert import table_to_xml


def main():
    dynamic_load = DynamicLoad()
    # csv1 = CSVReader()
    # csv1.load_excel(r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\dati_geologici_database\IsolineInfo.xlsx")
    # a = csv1.data.iloc[[1,2,3,4], :]
    # print (a)
    # nomi_col= list(a)
    # elemento = csv1.data[nomi_col[9]][1]
    # print("elemento nella tabella: " + str(elemento))
    # nuovo_elemento = parse_method_element(elemento)
    # print ("elemento dopo la trasformazione: " + str(nuovo_elemento))


    opened_connection = Connection()

    if not Connection.check_connection(opened_connection.connection):
        return logging.info("Error in connection")

    clear_schema(opened_connection.connection)

    boostrap_schema = BoostrapSchema()
    boostrap_schema.execute_query(opened_connection.connection)
    boostrap_schema.commit_query(opened_connection.connection)

    lista_faglie = [[5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [],
                    [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]]
    lista_colonne_excel = [[], [], [], [0, 1, 3, 4, 5, 6], [0, 1, 3, 4], [], [0, 1, 2, 3, 4, 6, 8, 9, 10, 11, 12]]
    mapper_cycle(opened_connection.connection, lista_faglie)

    # excel_list = [ r"C:\Users\giuli\OneDrive\Desktop\Progetto "
    # r"ISPRA\Test_Dataset_PoBasin\dati_geologici_database\referencedGeologicUnit.xlsx",
    # r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\dati_geologici_database\Boundary.xlsx",
    # r"C:\Users\giuli\OneDrive\Desktop\Progetto "
    # r"ISPRA\Test_Dataset_PoBasin\dati_geologici_database\All_geologic_unit.xlsx",
    # r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\dati_geologici_database\Isoline.xlsx",
    # r"C:\Users\giuli\OneDrive\Desktop\Progetto
    # ISPRA\Test_Dataset_PoBasin\dati_geologici_database\PL_u_contour.xlsx",
    # r"C:\Users\giuli\OneDrive\Desktop\Progetto "
    # r"ISPRA\Test_Dataset_PoBasin\dati_geologici_database\CompositionPart1.xlsx",
    # r"C:\Users\giuli\OneDrive\Desktop\Progetto "
    # r"ISPRA\Test_Dataset_PoBasin\dati_geologici_database\geochronologicEra1.xlsx"]



    name_faglie = [' Faults', 'FaultsShp','FaultsAll3d']
    name_models = ['GeologicUnit', 'Boundary', 'BoundaryInfo', 'CompositionPart',
                   'GeologicalEvent', 'Isoline', 'IsolineInfo']

    # tabled = dynamic_load.to_dto(
    #     r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\dati_geologici_database\IsolineInfo.xlsx", "IsolineInfoDto", [0, 1, 2, 3, 4, 6, 8, 9, 10, 11,12])
    # print(tabled)
    # faults_mapper = IsolineInfoMapper()
    # models = faults_mapper.to_model_list_isoline_info(tabled)
    # print(models)
    # faults_repo = IsolineInfoRepo(opened_connection.connection)
    # faults_repo.populate_isoline_info(models)

    # table_to_xml("BoundaryInfo", "public", opened_connection.connection)



    close_connection(opened_connection.connection)


if __name__ == '__main__':
    main()
