
# importo la libreria “pandas” e la connessione al DataFrame MySQL con cui interagire ed Error che serve per gestire eccezioni legate al database
import pandas as pd
import mysql.connector
from mysql.connector import Error

#la seguente funzione si occupa di leggere i dati dal file Excel e inserirli nella tabella MySQL
def inserisci_dati_in_database(file_xlsx, host, user, password, database):
    connessione = None  # Inizializza connessione come None
    try:
        dati = pd.read_excel(file_xlsx) #legge il file Excel e lo carica in un DataFrame Pandas

        # Verifica se tutte le colonne richieste sono presenti nel file Excel e se mancano delle colonne, viene stampato un messaggio di errore e la funzione si interrompe
        colonne_richieste = {'nome', 'cognome', 'email', 'numero_telefono'}
        if not colonne_richieste.issubset(dati.columns):
            print(f"Errore: Il file Excel deve contenere le colonne {colonne_richieste}.")
            return

        # Connessione al database MySQL
        connessione = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        # Verifica della connessione
        if connessione.is_connected():
            cursor = connessione.cursor()
            print("Connessione al database riuscita.")

            # Query di inserimento dati
            query_inserimento = """
            INSERT INTO identita_random (nome, cognome, email, numero_telefono)
            VALUES (%s, %s, %s, %s)
            """

            # Iterazione sui dati ed inseriremento di ciascuna riga nel DataFrame
            for _, riga in dati.iterrows():
                try:
                    valori = (
                        str(riga['nome']),
                        str(riga['cognome']),
                        str(riga['email']),
                        str(riga['numero_telefono'])
                    )
                    cursor.execute(query_inserimento, valori)
                except Exception as ex:
                    print(f"Errore durante l'inserimento della riga: {ex}")

            # Conferma delle modifiche
            connessione.commit()
            print("Dati inseriti correttamente nella tabella.")
            # In caso di possibili errori, vengono mostrati determinati messaggi
    except FileNotFoundError:
        print(f"Errore: il file '{file_xlsx}' non è stato trovato. Verifica il percorso.")
    except Error as e:
        print("Errore durante la connessione al database MySQL:", e)
    finally:
        # Chiude la connessione
        if connessione and connessione.is_connected():
            try:
                cursor.close()
                connessione.close()
                print("Connessione al database chiusa.")
            except Error as e:
                print("Errore durante la chiusura della connessione:", e)

# Chiamata alla funzione
file_xlsx = 'identita_random.xlsx'
host = 'localhost'
user = 'root'
password = 'vincenzo'
database = 'identita'

inserisci_dati_in_database(file_xlsx, host, user, password, database)
