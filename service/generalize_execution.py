import logging
import pathlib
import ast

from repository.dao.bootstrap_schema import BoostrapSchema, mapper_cycle, clear_schema_all, clear_schema_geounit, \
    clear_schema_faults, remake_schema_procedure

from repository.reader.csv_reader import CSVReader
from repository.reader.shp_reader import SHPReader
from service import dynamic_load_service
from service.dynamic_load_service import DynamicLoad
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


# procedura1: elimina tutte le tabelle, le ricrea, e le riempie con i dati nei file excel nella cartella
# "dati_geologici_database"  prendendo le colonne di ognuno da lista_colonne_excel.


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def delete_query(connection, nome):
    delete_query = ''' DELETE FROM public."Procedure" WHERE nome = '%s' ''' % nome
    cursor = connection.cursor()
    cursor.execute(delete_query)
    connection.commit()


def genera_procedure(connection):
    dynamic_load = DynamicLoad()
    csvreader = CSVReader()

    comando = input(
        "Per eliminare tutte le tabelle nel database scrivere '1'; \nPer eliminare le tabelle nel database relative "
        "all'unità geologica scrivere '2'; \nPer eliminare le tabelle nel database relative alle faglie scrivere '3'; "
        "\nAltrimenti premere invio\n")
    if comando == "1":
        clear_schema_all(connection)

    elif comando == "2":
        clear_schema_geounit(connection)

    elif comando == "3":
        clear_schema_faults(connection)

    comando1 = input("Per creare tutte le tabelle nel database scrivi 'crea', altrimenti premi invio\n")
    if comando1 == "crea":
        boostrap_schema = BoostrapSchema()
        boostrap_schema.execute_query(connection)
        boostrap_schema.commit_query(connection)

    q1 = """ SELECT nome FROM public."Procedure" """
    lista_procedure = read_query(connection, q1)

    if lista_procedure == []:
        input("Non sono presenti procedure memorizzate. \nPremere invio per continuare con una procedura manuale\n")
        scelta_proc = "no"

    else:
        scelta_proc = input("Se vuoi usare una procedura già esistente digita 'si'\nAltrimenti premere invio\n")

    if scelta_proc == "si":
        print("Scegli una tra le seguenti procedure, riscrivendola esattamente com'è:\n")
        for i in lista_procedure:
            print(i)
        nome_proc = input(
            "Queste sono le procedure disponibili. Per sceglierne una riscrivila esattamente com'è:\n")
        q2 = """ SELECT * FROM public."Procedure" WHERE nome = '%s' """ % nome_proc
        extr_riga = read_query(connection, q2)
        riga_proc = extr_riga[0]
        listaexcel = riga_proc[2]
        listapath = riga_proc[3]
        colonne = riga_proc[4]
        listacolonne = []
        for j in range(0, len(colonne)):
            listacolonne.append(ast.literal_eval(colonne[j]))  # questo perchè ogni elemento della lista è una stringa
            # che contiene a sua volta una lista ("[1,2,3]", con literal_eval torna una lista, e quindi creo una
            # lista di liste)

    else:
        dire = pathlib.Path().resolve()
        print(dire)
        print(
            "Quello sopra riportato è il path della cartella in cui si trova l'eseguibile \nInserire i file excel che "
            "contengono i dati da inserire nel database in questa cartella \nDopo averlo fatto, chiudere questa "
            "finestra e riavviare l'eseguibile. \nSe i file erano già presenti all'avvio si può procedere con le "
            "prossime istruzioni")
        n = int(input("\nIndicare il numero di file excel da caricare\n"))
        print(
            "\nOra verrà chiesto di inserire il nome di ciascun file e quali colonne considerare \nInserire i nomi "
            "uno alla volta, nell'ordine in cui si desidera che vengano caricati \n")
        listapath = []
        listaexcel = []
        listacolonne = []
        listacolonneproc = []
        for i in range(0, n):
            nome = input("Inserisci il nome del file excel da caricare, inclusa la sua estensione\n")
            if nome[-5:] == ".xlsx":
                path = str(dire) + "\\" + nome
                listaexcel.append(nome)
                listapath.append(path)
            else:
                nome1 = input("Il file non è stato fornito nel formato corretto.\nRiprovare\n")
                if nome1[-5:] == ".xlsx":
                    path = str(dire) + "\\" + nome1
                    listaexcel.append(nome1)
                    listapath.append(path)
                else:
                    break  # ???

            csvreader.load_excel(path)
            nomi_col = list(csvreader.data)
            nomi_ind_col = []
            for h in range(0, len(nomi_col)):
                nomi_ind_col.append(nomi_col[h] + ": indice relativo= " + str(h))
            print(nomi_ind_col)  # per mostrare i nomi delle colonne del file e relativo indice

            input_col = input(
                "\nSopra sono mostrate le colonne (e il relativo indice) appartenenti al file scelto. Selezionare "
                "quali sono le colonne di interesse di " + nome + ": \nInserire 'all' se si vogliono tutte le "
                                                                  "colonne, oppure una lista con gli indici delle "
                                                                  "relative colonne \n")
            if input_col != 'all':
                ind_list = ast.literal_eval(input_col)  # per far diventare la stringa una lista
                lista_num_col = ind_list
            else:
                lista_num_col = []
            listacolonne.append(lista_num_col)
            listacolonneproc.append(str(lista_num_col))
        print('\nRiassunto delle informazioni fornite')
        print(listaexcel)
        print(listacolonne)

    for i in range(0, len(listaexcel)):
        file = listaexcel[i]
        path = listapath[i]
        lista_num_col = listacolonne[i]
        model_class_str = file[0:-5]
        file_dto = (model_class_str + "Dto")
        #TODO
        # info = input("Se per il file "+ file + "si vogliono caricare dati relativi alla geometria digitare "
        #                                        "'si'\nAltrimenti premere invio\n")
        # if info == "si":
        #     path_shp = "r"+ input ("Inserire il path dello shapefile da cui vanno caricati i dati\n")
        #     tabled = dynamic_load.to_dto_geom(path, path_shp, file_dto, lista_num_col)
        # else:
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

    if scelta_proc != "si":
        nome_meth = input("Si desidera salvare questa procedura?\n Se si, inserire il nome che si vuole dare alla "
                          "procedura, altrimenti digitare 'no'\nN.B.: NON si può inserire un nome già esistente\n")
        if nome_meth != "no":
            num_id = len(lista_procedure) + 1
            insert_query = """ INSERT INTO "Procedure"  (
                        "id",
                        "nome",
                        "listaFileExcel",
                        "listaPath",
                        "listaColonne") VALUES (%s, %s, %s, %s, %s)"""
            values_insert = (str(num_id), nome_meth, listaexcel, listapath, listacolonneproc)
            cursor = connection.cursor()
            cursor.execute(insert_query, values_insert)
            connection.commit()
            print("Procedura salvata correttamente.\n")

    comm_finale1 = input('Processo completato. \nPremi invio per chiudere la finestra.')
