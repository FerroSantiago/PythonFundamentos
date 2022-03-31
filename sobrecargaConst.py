class PruebaSobrecargaConstr:
    def __init__(self, *args):
        if len(args)>3:
            self.respuesta = "Mas de 3 arguementos"
        elif len(args)<=3:
            self.respuesta = "Menos de 3 argumentos"


p1 = PruebaSobrecargaConstr(1,2,3,4)
print(p1.respuesta)

p2 = PruebaSobrecargaConstr(1,2)
print(p2.respuesta)