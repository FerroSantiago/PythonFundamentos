from calendar import c
from inspect import classify_class_attrs


class Auto:
    def __init__(self, patente, colorExterior):
        self.patente = patente
        self.colorExterior = colorExterior

autito = Auto("qjs789", "Rojo")
print(autito.patente, autito.colorExterior)



class Mercedes(Auto):
     def __init__(self, patente, colorExterior, colorInterior):
         Auto.__init__(self, patente, colorExterior)
         self.colorInterior = colorInterior

amg = Mercedes("ae372xz", "Negro", "Negro")
print(amg.patente, amg.colorExterior, amg.colorInterior)



class Volkswagen(Auto):
     def __init__(self, patente, colorExterior, colorLlantas):
         Auto.__init__(self, patente, colorExterior)
         self.colorLlantas = colorLlantas

gol = Volkswagen("xtz990", "Azul", "Cromadas")
print(gol.patente, gol.colorExterior, gol.colorLlantas)



class Renault(Auto):
         def __init__(self, patente, colorExterior, techo):
             Auto.__init__(self, patente, colorExterior)
             self.techo = techo

megane = Renault("mao841", "Gris", "Removible")
print(megane.patente, megane.colorExterior, megane.techo)

