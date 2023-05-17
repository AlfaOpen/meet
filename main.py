import cmd
import logging
import os

from dto.boundary_info_dto import BoundaryInfoDto
from dto.isoline_dto import IsolineDto
from mapper.boundary_info_mapper import BoundaryInfoMapper
from mapper.boundary_mapper import BoundaryMapper
from mapper.composition_part_mapper import CompositionPartMapper
from mapper.geologic_unit_mapper import GeologicUnitMapper
from mapper.geological_event_mapper import GeologicalEventMapper
from mapper.isoline_info_mapper import IsolineInfoMapper
from mapper.isoline_mapper import IsolineMapper
from model.boundary_info import BoundaryInfo
from repository.connection.connection import Connection, close_connection
from repository.dao.bootstrap_schema import BoostrapSchema, mapper_cycle
from repository.dao.boundary_info_repository import BoundaryInfoRepo
from repository.dao.boundary_repository import BoundaryRepo
from repository.dao.composition_part_repository import CompositionPartRepo
from repository.dao.geologic_unit_repository import GeologicUnitRepo
from repository.dao.geological_event_repository import GeologicalEventRepo
from repository.dao.isoline_info_repository import IsolineInfoRepo
from repository.dao.isoline_repository import IsolineRepo
from repository.dynamic_load.dynamic_load import DynamicLoad
from repository.reader.csv_reader import CSVReader

import pandas


def main():
    dynamic_load = DynamicLoad()
    # csv1 = CSVReader()
    # csv1.load_excel(r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\tabelle\Isoline.xlsx")
    # a = csv1.data.iloc [:, [1,3]]
    # print(csv1.data)
    # print(a)

    opened_connection = Connection()

    if not Connection.check_connection(opened_connection.connection):
        return logging.info("Error in connection")

    # boostrap_schema = BoostrapSchema()
    # boostrap_schema.execute_query(opened_connection.connection)
    # boostrap_schema.commit_query(opened_connection.connection)
    lista = os.listdir(r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\dati_geologici_database")
    lista.insert(0, 'abc')
    print(lista)

    for i in lista:
        if i == "GeologicUnit.xlsx":
            print(i)
            lista.insert(0, i)
            break
    print(lista)


    # for i in range(0, len(lista)):
    #     file = lista[i]
    #     path = "C:\\Users\\giuli\\OneDrive\\Desktop\\Progetto ISPRA\\Test_Dataset_PoBasin\\dati_geologici_database\\" + file
    #     # a = "ciao.xlsx"
    #     model_class_str = file[0:-5]

    # a = "C:\\Users\\giuli\\OneDrive\\Desktop\\Progetto ISPRA\\Test_Dataset_PoBasin\\dati_geologici_database\\"+ lista [0]
    # csv = CSVReader()
    # csv.load_excel(a)
    # print(csv.data)
    # col= input ('Inserisci una lista contenente gli indici delle colonne che vuoi inserire')
    #
    # file = lista[0]
    # model_class_str = file[0:-5]
    # print(model_class_str)


    # excel_list = [
    #     r"C:\Users\giuli\OneDrive\Desktop\Progetto "
    #     r"ISPRA\Test_Dataset_PoBasin\dati_geologici_database\referencedGeologicUnit.xlsx",
    #     r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\dati_geologici_database\Boundary.xlsx",
    #     r"C:\Users\giuli\OneDrive\Desktop\Progetto "
    #     r"ISPRA\Test_Dataset_PoBasin\dati_geologici_database\All_geologic_unit.xlsx",
    #     r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\dati_geologici_database\Isoline.xlsx",
    #     r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\dati_geologici_database\PL_u_contour.xlsx",
    #     r"C:\Users\giuli\OneDrive\Desktop\Progetto "
    #     r"ISPRA\Test_Dataset_PoBasin\dati_geologici_database\CompositionPart1.xlsx",
    #     r"C:\Users\giuli\OneDrive\Desktop\Progetto "
    #     r"ISPRA\Test_Dataset_PoBasin\dati_geologici_database\geochronologicEra1.xlsx"]

    lista_colonne_excel = [[], [], [], [], [1, 2, 5], [0, 1, 3, 4, 5, 6], [0, 1, 3, 4]]
    name_models = ['GeologicUnit', 'Boundary', 'BoundaryInfo', 'Isoline', 'IsolineInfo', 'CompositionPart',
                   'GeologicalEvent']

    # mapper_cycle(excel_list, lista_colonne_excel, name_models, opened_connection.connection)

    close_connection(opened_connection.connection)
    print("Table created successfully in PostgresSQL ")


if __name__ == '__main__':
    main()
