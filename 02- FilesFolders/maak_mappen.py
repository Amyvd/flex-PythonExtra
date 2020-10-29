import os
bestand = open("Klasgenoten.txt", "r")



tekst_regel = bestand.readline()
print(tekst_regel)

while tekst_regel:
    tekst_regel = tekst_regel.strip()
    print(tekst_regel)
    tekst_regel = bestand.readline()





