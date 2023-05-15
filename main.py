import logging

from dto.boundary_info_dto import BoundaryInfoDto
from dto.isoline_dto import IsolineDto
from mapper.isoline_mapper import IsolineMapper
from model.boundary_info import BoundaryInfo
from repository.connection.connection import Connection, close_connection
from repository.dao.bootstrap_schema import BoostrapSchema
from repository.dao.isoline_repository import IsolineRepo
from repository.dynamic_load.dynamic_load import DynamicLoad
from repository.reader.csv_reader import CSVReader

import pandas

from utility.parser import Parser


def main():

    dynamic_load = DynamicLoad()
    # csv1 = CSVReader()
    # csv1.load_excel(r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\tabelle\Isoline.xlsx")
    # csv1.num_rows(csv1.data)
    # print(csv1.data)
    # print(csv1.nrows)
    opened_connection = Connection()

    if not Connection.check_connection(opened_connection.connection):
        return logging.info("Error in connection")

    boostrap_schema = BoostrapSchema()
    boostrap_schema.execute_query(opened_connection.connection)
    boostrap_schema.commit_query(opened_connection.connection)

    tabled = dynamic_load.to_dto(r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\tabelle\Isoline.xlsx", "IsolineDto")

    isoline_mapper = IsolineMapper()
    models = isoline_mapper.to_model_list(tabled)
    print(models)


    isoline_repo = IsolineRepo(opened_connection.connection)
    isoline_repo.populate_isoline(models)

    close_connection(opened_connection.connection)
    print("Table created successfully in PostgresSQL ")


if __name__ == '__main__':
    main()
