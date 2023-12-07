#!/usr/bin/env python3


import os

current_directory = os.path.dirname(os.path.abspath(__file__))

files_in_directory = os.listdir(current_directory)

csv_files = [file for file in files_in_directory if file.endswith('.csv')]

if len(csv_files) == 0:
    print("Wrapped playlist not found.\nGo to https://watsonbox.github.io/exportify/ and download the playlist as .csv file to this folder.")
else:
    filenumber = 1
    numbering = {}

    print("Which file do you want to search?")
    for file in csv_files:
        print(f"{filenumber}. {file}")
        numbering[filenumber] = file
        filenumber += 1
    
    wrapped = numbering[int(input("Input the number: "))]

    while True:
        number = int(input("Input a number between 1-100 (0 will stop the program): "))
        if number == 0:
            break

        with open(wrapped) as csv:
            content = csv.readlines()
            
        song_info = content[number].split('","')
        song = str(song_info[3]) + ": " + str(song_info[1])
        release_year = str(song_info[8][:4])
        url = str(song_info[0][15:])
        print(song, "(" + release_year + ")" + "\n" + "https://open.spotify.com/track/" + url)
