import psycopg2
import logging


def create_connection():
    pass


class CreateConnection:
    connection = create_connection()

    @classmethod
    def create_connection():
        return psycopg2.connect(user="giulia",
                                password="password",
                                host="127.0.0.1",
                                port="5432",
                                database="postgres")

    @classmethod
    def close_connection(connection):
        if connection:
            connection.close()
        logging.info('Connection closed')
