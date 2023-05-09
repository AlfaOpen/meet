from repository.connection.connection import CreateConnection


def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    connection1 = CreateConnection
    cursor = connection1.connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE mobile
            (ID INT PRIMARY KEY     NOT NULL,
            MODEL           TEXT    NOT NULL,
            PRICE         REAL); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection1.connection.commit()
    connection1.close_connection()
    print("Table created successfully in PostgresSQL ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
