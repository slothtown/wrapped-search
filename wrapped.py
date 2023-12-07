#!/usr/bin/env python3


import os

current_directory = os.path.dirname(os.path.abspath(__file__))

files_in_directory = os.listdir(current_directory)

csv_files = [file for file in files_in_directory if file.endswith('.csv')]

if len(csv_files) == 0:
    print("Wrapped-soittolistaa ei löydy.\nMene sivulle https://watsonbox.github.io/exportify/ ja lataa soittolista csv-muodossa tähän kansioon.")
else:
    tiedostonumero = 1
    numerointi = {}

    print("Mitä Wrapped-soittolistaa käytetään?")
    for file in csv_files:
        print(f"{tiedostonumero}. {file}")
        numerointi[tiedostonumero] = file
        tiedostonumero += 1
    
    wrapped = numerointi[int(input("Syötä numero: "))]

    while True:
        numero = int(input("Anna numero väliltä 1-100 (0 lopettaa): "))
        if numero == 0:
            break

        with open(wrapped) as tiedosto:
            sisältö = tiedosto.readlines()
            
        kappaletiedot = sisältö[numero].split('","')
        kappale = str(kappaletiedot[3]) + ": " + str(kappaletiedot[1])
        vuosi = str(kappaletiedot[8][:4])
        url = str(kappaletiedot[0][15:])
        print(kappale, "(" + vuosi + ")" + "\n" + "https://open.spotify.com/track/" + url)
