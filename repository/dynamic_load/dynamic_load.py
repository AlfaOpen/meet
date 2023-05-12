from dto.boundary_info_dto import BoundaryInfoDto
from repository.reader.csv_reader import CSVReader


class DynamicLoad:

    def to_dto(self, path, filename, file_dto,
               file_mapper):  # filename è il nome della tabella excel, file dto è il nome del file dto che ogliamo riempire
        csv = CSVReader()
        csv.load_excel(path)
        csv.num_rows(csv.data)
        nomi_col = list(csv.data)
        k: int
        for i in csv.nrows:
            istanza = globals()[file_dto]()
            riga = csv.data[csv.data.index == i]
            k = 0
            while k < len(nomi_col):
                metodo_str = "set_" + list(csv.data)[k]
                metodo = getattr(istanza, metodo_str)
                metodo(riga[list(csv.data)[k]])
                k += 1
