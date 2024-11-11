class Varasto:
    def __init__(self, tilavuus, alku_saldo=0):
        self.tilavuus = max(tilavuus, 0.0)
        self.saldo = max(min(alku_saldo, tilavuus), 0.0)

    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara >= 0:
            self.saldo = min(self.saldo + maara, self.tilavuus)

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            maara = self.saldo
            self.saldo = 0.0
        else:
            self.saldo -= maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
