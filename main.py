# Lari Wihuri

from time import sleep
import focar

# Ajo-ohjeet listassa
komennot = []

# Aikamuuttujat ajoon ja kääntymiseen
ajo_aika = 2
kaantymis_aika = 0.75

# Luetaan ajo-ohjeet ja lisätään ne komennot listaan
try:
    with open("ajo_ohjeet.txt", "r") as ohjeet:
        for rivi in ohjeet: # Käydään ohjeet rivi kerrallaan läpi
            komento = rivi.strip().lower() # Tallennetaan komento muuttujaan, poistetaan välit ja muutetaan pieniksi kirjaimiksi
            if komento: # Jos komento EI ole tyhjä, lisätään se komennot listaan
                komennot.append(komento)
except:
    print("Virhe ohjetiedoston avauksessa.") # Tulostetaan virhe, jos ohjetiedostoa ei voitu avata

# Asetetaan auton nopeus
focar.nopeuden_vaihto(80)

# Suoritetaan komennot listasta ja ajetaan reitti
try:
    for komento in komennot:

        print ("Suoritetaan komento: ", komento)

        if komento == "eteen":
            focar.nopeuden_vaihto(80)
            focar.eteen(ajo_aika)
        elif komento == "taakse":
            focar.nopeuden_vaihto(80)
            focar.taakse(ajo_aika)
        elif komento == "vasen":
            focar.nopeuden_vaihto(80)
            focar.vasen(kaantymis_aika)
        elif komento == "oikea":
            focar.nopeuden_vaihto(80)
            focar.oikea(kaantymis_aika)
        elif komento == "led_on":
            focar.led_paalle()
        elif komento == "led_off":
            focar.led_pois_paalta()
        elif komento == "pysahdy":
            focar.pysahdy()
        else:
            print ("Tuntematon komento.")

        focar.pysahdy() # Pysähdytään ajokomentojen välissä
        sleep(1) # Sekunnin tauko ajokomentojen välissä

except:
    print("Virhe komentojen suorituksessa.") # Tulostetaan virhe, jos komennon suorittaminen epäonnistuu

finally:
    # Pysäytetää auto lopuksi
    focar.pysahdy()
    print("Ajo suoritettu.")