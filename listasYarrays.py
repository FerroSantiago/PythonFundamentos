medicamentos = []
informacionpedido = []
fecha = str(input("Ingrese la fecha en la que se realiza el pedido de medicamentos(dd/mm/aa): "))
informacionpedido.append(fecha)
nombre = str(input("Ingrese el nombre del médico que prescribió la receta: "))
informacionpedido.append(nombre)
medicamento = str(input("Ingresar un medicamento: "))
informacionpedido.append(medicamento)
opcion = int(input("Agregar otro medicamento: 1- Agregar 0- Finalizar pedido "))
while opcion == 1:
    medicamento = str(input("Ingresar el medicamento: "))
    informacionpedido.append(medicamento)
    opcion = int(input("Agregar otro medicamento: 1- Agregar 0- Finalizar pedido "))
medicamentos.append(informacionpedido) 

num = 0
for posicion in medicamentos:
    num = num + 1
    print()
    print("Pedido de medicamentos numero", num, ": ")
    print("Fecha: ", posicion[0])
    print("Nombre del médico que prescribió la receta: ", posicion[1])
    print("Medicamentos: ", posicion[2:])
    print()