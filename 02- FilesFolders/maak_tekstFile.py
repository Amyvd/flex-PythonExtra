import io

#zo open je een bestand om naar te schrijven 
bestand = open("test.text", "w")

#een tekst naar de bestand schrijven
bestand.write("Test 123!");

#vergeet dit bestand niet te sluiten
bestand.close()

#___________________________________________________________________

#bestand in read.only (r) mode openen
bestand2 = open("test.text", "r")

#een tekst naar het bestand schrijven
bestand2.write("Lekker alles aan het overschrijven")

#_________________________________________________________________________

import io
#bestand in read-only (R) mode openen
bestand2 = open("test.text", "r")
inhoud = bestand2.read()
print("De inhoud van het bestand is:")
print(inhoud)

