#importo la libreria Faker per generare dati casuali, come nomi, cognomi, email e numeri di telefono
#Importo la libreria Pandas per manipolazione e gestione dei dati in tabella, con lo scopo di creare e salvare i dati generati in un file Excel

from faker import Faker
import pandas as pd

# qui viene inizializzato il generatore di dati casuali tramite la libreria “Faker” usando il formato e lo stile italiano, dove “it” è il codice per l’Italia e “IT” rappresenta il paese secondo lo standard ISO 639-1
fake = Faker('it_IT')

# In questa fase viene inizializzata una lista vuota per memorizzare i dati
identities = []

# Qui vengono generati 10 identità casuali attraverso un ciclo for, a ogni iterazione viene creato un dizionario identity dove abbiamo nome, cognome, email e numero di telefono, ogni identità viene aggiunta poi alla lista identities
for _ in range(10):
    identity = {
        "nome": fake.first_name(),
        "cognome": fake.last_name(),
        "email": fake.email(),
        "numero_telefono": fake.phone_number()
    }
    identities.append(identity)

# I dati della lista identities vengono convertiti in un DataFrame Pandas, così da essere rappresentati come tabella strutturata simile a un foglio di calcolo
df = pd.DataFrame(identities)

# Il file che viene salvato in Excel viene rinominato “identita_random.xlsx” e il DataFrame df viene salvato in formato Excel usando to_excel(), con index=False per escludere l’indice delle righe.
file_name = "identita_random.xlsx"
df.to_excel(file_name, index=False)

# al termine del programma, viene stampato un messaggio di conferma
print(f"File Excel '{file_name}' creato con successo!")
