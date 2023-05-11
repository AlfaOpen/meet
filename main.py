import logging

from repository.connection.connection import Connection, close_connection
from repository.dao.bootstrap_schema import BoostrapSchema
from repository.reader.csv_reader import CSVReader


def main():
    csv = CSVReader(10)
    filename = r'C:\Users\giuli\Desktop\Progetto ISPRA\Test_Dataset_PoBasin\BoundaryInfo\CSV\TE_u_east.csv'
    csv.load_csv(filename)
    print(csv.data.values)

    # csv.retrieve_column(csv.data, ['2'])
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
