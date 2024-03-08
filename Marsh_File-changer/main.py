import os
import shutil

# Ścieżka do folderu, z którego chcesz odczytać nazwy plików
folder_zrodlowy = r"C:\Users\podci\PycharmProjects\100projects\Marsh_File-changer"+r"\folder1"

# Ścieżka do folderu docelowego (folder 2)
folder_docelowy = r"C:\Users\podci\PycharmProjects\100projects\Marsh_File-changer"+r"\folder2"

# lista plików w folderze (PLIKI DO PRZERZUCENIA)
pliki_1 = os.listdir(folder_zrodlowy)

# lista foldery w folderze docelowym
foldery = os.listdir(folder_docelowy)


# pętla po plikach docelowych
try:
    for folder in foldery:
        #pętla po plikach źródłowych

        for plik in pliki_1:
            #prównywanie nazwy firmy do nazwy folderu firmy
            nazwa_firmy =plik.split(',')
            nazwa_firmy = nazwa_firmy[1].strip()

            if nazwa_firmy.lower() == folder.lower():
                shutil.move(f'{folder_zrodlowy}\{plik}', f'{folder_docelowy}\{folder}')

except IndexError:
    print("Coś poszło nie tak z indeksowaniem, sprawdz czy nazwa plików zawiera przecinki, jeżeli tak to...Lepiej "
          "zawołaj informatyka!")
