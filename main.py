import logging

from repository.connection.connection import Connection, close_connection
from repository.dao.bootstrap_schema import BoostrapSchema
from repository.reader.csv_reader import CSVReader

import pandas

def main():
    csv = CSVReader(10)
    import openpyxl
    filename = r"C:\Users\giuli\OneDrive\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\BoundaryInfo\top_Carb_west.xlsx"
    csv.load_excel(filename)
    print(csv.data)
    riga = csv.data[csv.data.index == 1]
    print(list(csv.data))
    # print (riga['Name'][3])


    # print(csv.data)
    # csv.retrieve_column(csv.data, ['Id', 'x', 'Name'])
    # print(csv.column_data)



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
