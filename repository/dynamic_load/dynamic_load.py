from dto.boundary_dto import BoundaryDto
from dto.boundary_info_dto import BoundaryInfoDto
from dto.composition_part_dto import CompositionPartDto
from dto.faults_dto import FaultsDto
from dto.faults_shp_dto import FaultsShpDto
from dto.geologic_unit_dto import GeologicUnitDto
from dto.geological_event_dto import GeologicalEventDto
from dto.isoline_dto import IsolineDto
from dto.isoline_info_dto import IsolineInfoDto


from repository.reader.csv_reader import CSVReader
import openpyxl

from utility.parser import parse_method_name


class DynamicLoad:

    def to_dto(self, path, file_dto, index_col):  # file dto è il nome del file dto che vogliamo riempire,
        # name_column è la lista di colonne della tabella excel che vogliamo prendere (Nel caso non servissero tutte)
        csv = CSVReader()
        csv.load_excel(path)
        csv.num_rows(csv.data)
        if index_col is None or len(index_col) == 0:
            nomi_col = list(csv.data)
        else:
            colonne = csv.data.iloc[:, index_col]
            nomi_col = list(colonne)
        tabella = []
        k: int
        for i in range(0, csv.nrows):
            istanza = globals()[file_dto]()  # inizializzo un'istanza della classe file_dto, in particolare una
            # diversa per ogni riga, quindi scorrendo nel ciclo riempio tutte le righe
            riga = csv.data[csv.data.index == i]
            k = 0
            while k < len(nomi_col):
                str_par = parse_method_name(nomi_col[k])
                metodo_par = "set_" + str_par
                metodo = getattr(istanza, metodo_par)
                metodo(csv.data[nomi_col[k]][i])
                k += 1
            tabella.append(istanza)
        return tabella
