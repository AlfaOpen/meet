import psycopg2
import logging


class Connection:
    connection = None

    def __init__(self):
        self.connection = create_connection_postgis()

    @classmethod
    def check_connection(cls, connection):
        if connection is not None:
            return True
        else:
            return False


def create_connection():
    return psycopg2.connect(user="giulia",
                            password="password",
                            host="127.0.0.1",
                            port="5432",
                            database="postgres")

def create_connection_postgis():
    return psycopg2.connect(user="giulia",
                            password="password",
                            host="127.0.0.1",
                            port="5433",
                            database="postgres")


def close_connection(connection):
    if connection:
        connection.close()
    logging.info('Connection closed')

