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

    opened_connection = Connection()

    if not Connection.check_connection(opened_connection.connection):
        return logging.info("Error in connection")

    clear_schema(opened_connection.connection)

    boostrap_schema = BoostrapSchema()
    boostrap_schema.execute_query(opened_connection.connection)
    boostrap_schema.commit_query(opened_connection.connection)
    #
    lista_faglie = [[5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [],
                    [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]]
    lista_colonne_excel = [[], [], [], [0, 1, 3, 4, 5, 6], [0, 1, 3, 4], [], [0, 1, 2, 3, 4, 6, 8, 9, 10, 11, 12]]

    mapper_cycle(opened_connection.connection, lista_colonne_excel)
    # DIFFERENZE TRA CARICAMENTO UNIT E FAGLIE: cambiare la lista nel mapper, cambiare i due percorsi all'interno
    # della funzione mapper

    name_faglie = [' Faults', 'FaultsShp','FaultsAll3d']
    name_models = ['GeologicUnit', 'Boundary', 'BoundaryInfo', 'CompositionPart',
                   'GeologicalEvent', 'Isoline', 'IsolineInfo']

    # table_to_xml("FaultsAll3d", "public", opened_connection.connection)

    close_connection(opened_connection.connection)


if __name__ == '__main__':
    main()
