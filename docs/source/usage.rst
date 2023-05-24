Usage
=====

.. connection, struttura tabelle e relativa creazione (BoostrapSchema)
caricamento dati (csv reader e dynamic_load)
Mapping to models
Metodi di Insert
Conversione in xml

Connessione e Creazione delle tabelle
-------------------------------------

Si può utilizzare la classe ``Connection()`` e i relativi metodi per effettuare la connessione.

.. py:class:: Connection(connection)

    :attribute: ``connection``, richiama una funzione che apre la connessione al database postgres.

    :classmethod: ``check_connection()``, verifica appunto la connessione.

    La connessione può essere chiusa mediante ``close_connection()`` fornendogli in ingresso la connessione.

Nella classe ``BoostrapSchema`` vengono definite le query per la creazione delle tabelle.

.. py:class:: BoostrapSchema(table_list)

    :attribute: ``table_list``, una lista appunto contenente delle funzioni, ognuna delle quali contiene la query per la creazione della relativa tabella.

    :classmethod: ``execute_query()`` prende in ingresso la connessione ed esegue la query per ogni tabella all'interno della lista.

    :classmethod: ``commit_query()``

Caricamento Dati
---------


