import pandas


class CSVReader:

    def __init__(self):
        self.nrows = None
        self.data = None
        self.column_data = []
        # self.chunk = chunk

    # def load_csv(self, path):
    #     self.data = pandas.read_csv(path, chuncksize=self.chunk, on_bad_lines='skip', encoding="latin-1")
    #     return self.data

    def load_excel(self, path):
        self.data = pandas.read_excel(path, header=0)
        return self.data

    def num_rows(self, csv_data):  # calcola il numero di righe dell'excel
        self.nrows = len(csv_data.index)

    def retrieve_column(self, csv_data, column):
        self.column_data = pandas.DataFrame(csv_data, columns=column)

