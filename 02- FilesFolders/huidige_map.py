#hier importeer je de os module
import os

# de huidige directory opvragen en opslaan in de variabele : werkmap
werkmap = os.getcwd()

#De letters cwd staan voor: current working directory (de huidige map!)

# op het scherm printen
print("De huidige map is:" + werkmap)

os.mkdir("Een nieuwe map")

#Gebruiker om de naam van de map vragen
mapnaam = input("Welkee naam wil je voor de map ")

#als de lengte van mapnaam > 0 is dan maken we de map
lengte_mapnaam = len(mapnaam)
if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
    print("De map" + mapnaam + "is gemaakt")
else:
    print("Je hebt geen naam ingevoerd")
    



