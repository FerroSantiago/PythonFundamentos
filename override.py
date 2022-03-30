class Vehiculo():
    def __init__(self, color):
        self.color = color
    def infoRelevante(self):
        print("La informacion relevante es el color:", self.color)

vehiculo = Vehiculo("gris")
vehiculo.infoRelevante()

class Auto(Vehiculo):
    def __init__(self, color, ruedas):
            Vehiculo.__init__(self, color)
            self.ruedas = ruedas
    def infoRelevante(self):
        print("La informacionh relevante es la cantidad de ruedas:", self.ruedas)

auto = Auto("gris", "4")
auto.infoRelevante()