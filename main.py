import logging

from dto.boundary_info_dto import BoundaryInfoDto
from model.boundary_info import BoundaryInfo
from repository.connection.connection import Connection, close_connection
from repository.dao.bootstrap_schema import BoostrapSchema
from repository.reader.csv_reader import CSVReader

import pandas

from utility.parser import Parser


def main():
    csv = CSVReader()
    import openpyxl
    filename = r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\BoundaryInfo\top_Carb_west.xlsx"
    csv.load_excel(filename)
    # print(csv.data)
    riga = csv.data[csv.data.index == 3]
    print(riga)

    # print (riga['Name'][3])
    # a = type(csv)

    #  ESEMPIO REFLECTION CON CLASSE E METODO
    # class MyClass:
    #
    #     def __init__(self):
    #         self.abc = 2
    #
    #     def sole(self):
    #         print("hello")

    # print(MyClass())

    # a = "MyClass"
    # instanza = locals()[a]()
    # print(instanza.abc)
    # metodo1 = "sole"
    # metodo2 = getattr(instanza, metodo1)
    # metodo2()

    # metodo = "set_" + list(csv.data)[1]
    # print(metodo)
    # nome = BoundaryInfoDto()
    # name = "BoundaryInfo"
    # istanza1 = globals()[name]()
    # metodo4 = getattr(istanza1, metodo)
    # (metodo4(2))
    # print(istanza1.get_x())

    # print(csv.data)
    # csv.retrieve_column(csv.data, ['Id', 'x', 'Name'])
    # print(csv.column_data)

    nome = "HelloIOhhhPm"
    parser = Parser()
    print(parser.parse_method_name(nome))

    opened_connection = Connection()

    if not Connection.check_connection(opened_connection.connection):
        return logging.info("Error in connection")

    boostrap_schema = BoostrapSchema()
    boostrap_schema.execute_query(opened_connection.connection)
    boostrap_schema.commit_query(opened_connection.connection)

    close_connection(opened_connection.connection)
    print("Table created successfully in PostgresSQL ")


if __name__ == '__main__':
    main()
