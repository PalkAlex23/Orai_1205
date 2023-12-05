import Csoport

adatokListaja = []
def beolvasas():
    beFajl = open("csoport.txt", "r", encoding="utf-8")
    # első sor
    beFajl.readline()
    # többi sor
    sorok = beFajl.readlines()
    for sor in sorok:
        # tisztott sor
        tisztitottsor = sor.strip()
        # eldabarolás
        daraboltsor = tisztitottsor.split("/")
        # példányosítás
        csoporttag = Csoport.Csoport(daraboltsor[0], daraboltsor[1], daraboltsor[2])
        # belefűzöm az objektumokat a listába
        adatokListaja.append(csoporttag)
    beFajl.close()


def kiir():
    for index in range(0, len(adatokListaja), 1):
        print(adatokListaja[index])
        # print(adatokListaja[index].nev+" "+str(adatokListaja[index].evfolyam)+" "+str(adatokListaja[index].atlag))


def sorokSzama():
    sorszam = len(adatokListaja)
    print(f"A tanulók száma: {sorszam}")


def megszamlalas():
    osszeg = 0
    for index in range(0, len(adatokListaja), 1):
        osszeg += adatokListaja[index].atlag
    if len(adatokListaja) == 0:
        atlag = 0
    else:
        atlag = osszeg / len(adatokListaja)
    print(f"A suli átlaga: {round(atlag, 2)}")


def elsosok():
    elsos = 0
    for index in range(0, len(adatokListaja), 1):
        if adatokListaja[index].evfolyam == 1:
            elsos += 1
    print(f"Elsősök osztály létszáma: {elsos}")


beolvasas()
kiir()
megszamlalas()
elsosok()
