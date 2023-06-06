import logging
import pathlib
import ast

from repository.dao.bootstrap_schema import clear_schema, BoostrapSchema, mapper_cycle
from repository.dynamic_load import dynamic_load
from repository.dynamic_load.dynamic_load import DynamicLoad
from utility.parser import parse_method_name

from mapper.faults_all3d_mapper import FaultsAll3dMapper
from mapper.faults_mapper import FaultsMapper
from mapper.faults_shp_mapper import FaultsShpMapper
from mapper.isoline_info_mapper import IsolineInfoMapper
from mapper.isoline_mapper import IsolineMapper
from mapper.boundary_info_mapper import BoundaryInfoMapper
from mapper.boundary_mapper import BoundaryMapper
from mapper.composition_part_mapper import CompositionPartMapper
from mapper.geologic_unit_mapper import GeologicUnitMapper
from mapper.geological_event_mapper import GeologicalEventMapper
from repository.dao.boundary_info_repository import BoundaryInfoRepo
from repository.dao.boundary_repository import BoundaryRepo
from repository.dao.composition_part_repository import CompositionPartRepo
from repository.dao.geologic_unit_repository import GeologicUnitRepo
from repository.dao.geological_event_repository import GeologicalEventRepo
from repository.dao.faults_all3d_repository import FaultsAll3dRepo
from repository.dao.faults_repository import FaultsRepo
from repository.dao.faults_shp_repository import FaultsShpRepo
from repository.dao.isoline_info_repository import IsolineInfoRepo
from repository.dao.isoline_repository import IsolineRepo


def execution_service(connection):
    dynamic_load = DynamicLoad()

    comando = input("Per eliminare tutte le tabelle nel database scrivi 'elimina', altrimenti premi invio\n")
    if comando == "elimina":
        clear_schema(connection)

    comando1 = input("Per creare tutte le tabelle nel database scrivi 'crea', altrimenti premi invio\n")
    if comando1 == "crea":
        boostrap_schema = BoostrapSchema()
        boostrap_schema.execute_query(connection)
        boostrap_schema.commit_query(connection)

    lista_faglie = [[5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], [],
                    [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]]
    lista_colonne_excel = [[], [], [], [0, 1, 3, 4, 5, 6], [0, 1, 3, 4], [], [0, 1, 2, 3, 4, 6, 8, 9, 10, 11, 12]]

    comando2 = input("Per riempire tutte le tabelle nel database scrivi 'insert', altrimenti premi invio\n")
    if comando2 == "insert":
        mapper_cycle(connection, lista_colonne_excel)

    dire = pathlib.Path().resolve()
    print(dire)
    print(
        "Quello sopra riportato è il path della cartella in cui si trova l'eseguibile \nInserire i file excel che contengono i dati da inserire nel database in questa cartella \nDopo averlo fatto, chiudere questa finestra e riavviare l'eseguibile")
    n = int(input("\nIndicare il numero di file excel da caricare\n"))
    print(
        "\nOra verrà chiesto di inserire il nome di ciascun file e quali colonne considerare \nInserire i nomi uno alla volta, nell'ordine in cui si desidera che vengano caricati \n")
    listapath = []
    listaexcel = []
    listacolonne = []
    for i in range(0, n):
        nome = input("Inserisci il nome del file excel da caricare, inclusa la sua estensione\n")
        if nome[-5:] == ".xlsx":
            path = str(dire) + "\\" + nome
            listaexcel.append(nome)
            listapath.append(path)
        else:
            print("Il file non è stato fornito nel formato corretto")
            break
        input_col = input(
            "Selezionare le colonne di " + nome + ": \nInserire 'all' se si vogliono tutte le colonne, oppure una "
                                                  "lista con gli indici delle relative colonne \n")
        if input_col != 'all':
            ind_list = ast.literal_eval(input_col)
            lista_num_col = ind_list
        else:
            lista_num_col = []
        listacolonne.append(lista_num_col)
    print('\nRiassunto delle informazioni fornite')
    print(listaexcel)
    print(listacolonne)

    for i in range(0, len(listaexcel)):
        file = listaexcel[i]
        path = listapath[i]
        lista_num_col = listacolonne[i]
        model_class_str = file[0:-5]
        file_dto = (model_class_str + "Dto")
        tabled = dynamic_load.to_dto(path, file_dto, lista_num_col)
        file_mapper = globals()[model_class_str + "Mapper"]()
        str_par1 = parse_method_name(model_class_str)
        metodo_par1 = "to_model_list_" + str_par1
        metodo1 = getattr(file_mapper, metodo_par1)
        models_list = metodo1(tabled)
        file_repo = globals()[model_class_str + "Repo"](connection)
        metodo_par2 = "populate_" + str_par1
        metodo2 = getattr(file_repo, metodo_par2)
        metodo2(models_list)
    print('Insert effettuate correttamente')

    comm_finale = input('Processo completato. \nPremi invio per chiudere la finestra.')
