class PruebaOverload():                        
    def overloading(self, variable):                    
        if type(variable) == int:                
            print ("Su variable es de tipo entero")        
        elif type(variable) == str:
            print ("Su variable es de tipo texto/str")
        else:
            print ("Ingreso una variable de tipo diferente a str/int")

prueba1 = PruebaOverload()
print()
prueba1.overloading(3)
prueba1.overloading("Texto")
prueba1.overloading(0.5)