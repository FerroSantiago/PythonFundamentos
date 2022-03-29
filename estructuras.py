opcion = int(input("Desea ingresar datos? 1- Si, 0- No  "))
print()
while opcion == 1:
    aire = int(input("Del 1 al 10 cual es la calidad del aire: "))
    agua = int(input("Del 1 al 10 cual es la calidad del agua: "))
    comida = int(input("Del 1 al 10 cual es la calidad de los alimentos que ingiere: "))
    suma = aire + agua + comida
    if suma < 10:
        print("Su salud podria verse afectada por su estilo de calidad de vida")
    elif suma > 20:
        print("Usted tiene una buena calidad de vida")
    else:
        print("Su calidad de vida es aceptable, pero podria mejorar")
    print()
    opcion = int(input("Desea ingresar datos? 1- Si, 0- No  "))
