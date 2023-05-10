from repository.reader.csv_reader import CSVReader


class DynamicLoad:

    def to_dto(self, filename, file_dto, file_mapper):
        csv = CSVReader()
        csv.load_excel(filename)
        csv.num_rows(csv.data)
        nomi_col = list(csv.data)
        for i in csv.nrows:
            riga = csv.data[csv.data.index == i]
            file_dto =
