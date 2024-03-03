class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutná!")

class Kotatko(Zviratko):
    def udelej_zvuk(self):
        print(f"{self.jmeno}: Mňau!")

class Stenatko(Zviratko):
    def udelej_zvuk(self):
        print(f"{self.jmeno}: Haf!")

zviratka = [Kotatko('Micka'), Stenatko('Azorek')]

for zviratko in zviratka:
    zviratko.udelej_zvuk()
    zviratko.snez('flákota')