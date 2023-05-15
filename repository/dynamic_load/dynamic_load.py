from dto.boundary_dto import BoundaryDto
from dto.boundary_info_dto import BoundaryInfoDto
from dto.composition_part_dto import CompositionPartDto
from dto.geologic_unit_dto import GeologicUnitDto
from dto.geological_event_dto import GeologicalEventDto
from dto.isoline_dto import IsolineDto
from dto.isoline_info_dto import IsolineInfoDto

from repository.reader.csv_reader import CSVReader
import openpyxl
from utility.parser import Parser

class DynamicLoad:

    def to_dto(self, path, file_dto):  # file dto è il nome del file dto che vogliamo riempire
        csv = CSVReader()
        parser = Parser()
        csv.load_excel(path)
        csv.num_rows(csv.data)
        nomi_col = list(csv.data)
        tabella = []
        k: int
        for i in range(0, csv.nrows):
            istanza = globals()[file_dto]()  #inizializzo un'istanza della classe file_dto, in particolare una diversa per ogni riga, quindi scorrendo nel ciclo riempio tutte le righe
            riga = csv.data[csv.data.index == i]
            print(riga)
            k = 0
            while k < len(nomi_col):
                str_par = parse_method_name(nomi_col[k])
                metodo_par = "set_" + str_par
                metodo = getattr(istanza, metodo_par)
                print(type(csv.data[nomi_col[k]][i]))
                metodo(csv.data[nomi_col[k]][i])
                k += 1
            tabella.append(istanza)
        return tabella

