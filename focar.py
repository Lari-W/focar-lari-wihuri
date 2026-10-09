# Lari Wihuri
# Focarin toiminnallisuus

## --- TARVITTAVAT MODUULIT --- ##

from machine import Pin, PWM
from time import sleep


## --- LAITTEISTON MUUTTUJAT JA ARVOT --- #

# Picon LED
led = Pin("LED", Pin.OUT)

# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)


## --- FOCARIN MOOTTORIEN / LEDIN FUNKTIOT --- ###

# Moottorien maksimiteho = 65534
# Moottorien nopeus 0-100 arvoksi
def nopeuden_vaihto(prosentti):
    nopeus = int((prosentti / 100) * 65534) # Kerrotaan moottorien maksimiarvo kokonaisluvulla 0-100
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)

# Eteenpäin ajo
def eteen(aika):
    m1.value(1)
    m2.value(1)
    sleep(aika)

# Taaksepäin ajo
def taakse(aika):
    m1.value(0)
    m2.value(0)
    sleep(aika)

# Kääntyminen vasemmalle
def vasen(aika):
    m1.value(1)
    m2.value(0)
    sleep(aika)

# Kääntyminen oikealle
def oikea(aika):
    m1.value(0)
    m2.value(1)
    sleep(aika)

# Pysähtyminen - Moottorien pysäytys
def pysahdy():
    nopeuden_vaihto(0)

# LED päälle
def led_paalle():
    led.on()

# LED pois päältä
def led_pois_paalta():
    led.off()