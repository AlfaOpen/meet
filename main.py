from repository.connection.connection import Connection
import logging


def main():
    opened_connection = Connection.connection

    if not Connection.check_connection(opened_connection):
        return logging.info("Error in connection")

    cursor = opened_connection.connection.cursor()
    create_table_query = '''CREATE TABLE mobile
            (ID INT PRIMARY KEY     NOT NULL,
            MODEL           TEXT    NOT NULL,
            PRICE         REAL); '''

    cursor.execute(create_table_query)
    opened_connection.connection.commit()
    opened_connection.close_connection()
    print("Table created successfully in PostgresSQL ")


if __name__ == '__main__':
    main()

