import logging
import pathlib
from array import array
import signal
import time
from ast import literal_eval

from mapper.isoline_info_mapper import IsolineInfoMapper
from model.boundary import Boundary
from repository.connection.connection import Connection, close_connection
from repository.dao.bootstrap_schema import BoostrapSchema, mapper_cycle, clear_schema_faults, clear_schema_geounit
from repository.dao.isoline_info_repository import IsolineInfoRepo
from repository.reader.shp_reader import SHPReader
from service import dynamic_load_service
from service.dynamic_load_service import DynamicLoad
from repository.reader.csv_reader import CSVReader
from service.generalize_execution import read_query, genera_procedure, delete_query
from utility.format_convert import table_to_xml
from service.execution_service import execution_service


def main():
    dynamic_load = DynamicLoad()

    opened_connection = Connection()

    if not Connection.check_connection(opened_connection.connection):
        return logging.info("Error in connection")

    # clear_schema_geounit(opened_connection.connection)
    # clear_schema_faults(opened_connection.connection)

    # drop_query = '''DROP TABLE if exists public."Geometry" '''
    # cursor = opened_connection.connection.cursor()
    # cursor.execute(drop_query)
    # opened_connection.connection.commit()
    # print('Le tabelle selezionate sono state eliminate')
    #
    # boostrap_schema = BoostrapSchema()
    # boostrap_schema.execute_query(opened_connection.connection)
    # boostrap_schema.commit_query(opened_connection.connection)

    lista_faglie = [[5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [],
                    [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]]
    lista_colonne_excel = [[], [], [], [0, 1, 3, 4, 5, 6],
                           [5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [],
                           [0, 1, 2, 3, 4, 6, 7, 8, 9, 10], [0, 1, 3, 4], [], [0, 1, 2, 3, 4, 6, 8, 9, 10, 11, 12]]
    #  nella lista_colonne_excel ci sono le colonne di tutte le tabelle (unit + faglie) dove le faglie iniziano dopo composition part seguendo l'ordine alfabetico con cui le carica nel programma

    lista_geo_unit = [[], [], [0, 1, 2, 3, 4, 8], [0, 1, 3, 4, 5, 6], [0, 1, 3, 4], [],
                      [0, 1, 2, 3, 4, 6, 8, 9, 10, 11, 12]]
    # mapper_cycle(opened_connection.connection, lista_colonne_excel)
    # DIFFERENZE TRA CARICAMENTO UNIT E FAGLIE: cambiare la lista nel mapper, cambiare i due percorsi all'interno
    # della funzione mapper

    name_faglie = [' Faults', 'FaultsAll3d', 'FaultsShp']
    name_models = ['GeologicUnit', 'Boundary', 'BoundaryInfo', 'CompositionPart',
                   'GeologicalEvent', 'Isoline', 'IsolineInfo']

    # execution_service(opened_connection.connection)

    # genera_procedure(opened_connection.connection)

    # shp1= SHPReader()
    # shp1.shp_reader(r"C:\Users\giuli\Documents\shp_da_faultsAll.shp")


    # delete_query(opened_connection.connection,"insert_geounit")

   # table_to_xml("FaultsAll3d", "public", opened_connection.connection)

    close_connection(opened_connection.connection)


if __name__ == '__main__':
    main()
