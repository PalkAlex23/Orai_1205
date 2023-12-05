class Csoport:
    def __init__(self, nev: str, evfolyam, atlag):
        self.nev = nev
        daraboltNev = nev.split(" ")
        self.vezeteknev = daraboltNev[0]
        self.keresztnev = daraboltNev[1]

        self.evfolyam = int(evfolyam)

        atlag = atlag.replace(",", ".")
        self.atlag = float(atlag)

    def __str__(self) -> str:
        return f"Név: {self.nev}, évfolyam: {self.evfolyam}, átlaga: {self.atlag}"

