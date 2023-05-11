import pandas


class CSVReader:

    def __init__(self, chunk):
        self.data = None
        self.column_data = {}
        self.chunk = chunk

    def load_csv(self, path):
        self.data = pandas.read_csv(path, chunksize=self.chunk, on_bad_lines='skip', encoding="latin-1")
        return self.data

    def retrieve_column(self, csv_data, column):
        pandas.DataFrame(csv_data, columns=column)

