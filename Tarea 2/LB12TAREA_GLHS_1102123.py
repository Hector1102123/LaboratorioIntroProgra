#Hector Sebastian Garrido Lopez 1102123

print("Tarea 12")

class operaciones():
    Primer_Numero=""
    Segundo_Numero=""
    Suma=""
    Resta=""
    Multiplicacion=""
    Division=""

    def insertar_numero1(self, Primer_Numero):
        self.Primer_Numero=Primer_Numero
        
    def devolver_numero1(self):
        return self.Primer_Numero
    
    def insertar_numero2(self, Segundo_Numero):
        self.Segundo_Numero=Segundo_Numero

    def devolver_numero2(self):
        return self.Segundo_Numero
    
    def insertar_suma(self, Suma):
        self.Suma=Suma
        
    def devolver_suma(self):
        return self.Suma
    
    def insertar_resta(self, Resta):
        self.Resta=Resta
        
    def devolver_resta(self):
        return self.Resta
    
    def insertar_multiplicacion(self, Multiplicacion):
        self.Multiplicacion=Multiplicacion
        
    def devolver_multiplicacion(self):
        return self.Multiplicacion
    
    def insertar_division(self, Division):
        self.Division=Division
        
    def devolver_division(self):
        return self.Division

operaciones1=operaciones()
ingrese_numero1=float(input("Ingrese un numero:"))
ingrese_numero2=float(input("Ingrese un segundo numero:"))
Suma=ingrese_numero1+ingrese_numero2
Resta=ingrese_numero1-ingrese_numero2
Multiplicacon=ingrese_numero1*ingrese_numero2
Division=ingrese_numero1/ingrese_numero2
print("Si desea realizar una suma marque 1, si desea realizar una resta marque 2, si desea realizar una multiplicación marque 3, si desea realizar una división marque 4 y si desea salir marque 5.")
Condicion=True
while Condicion==True:
    Valor_deseado=int(input("Ingrese el valor que desea:"))
    if Valor_deseado==1:
        operaciones1.insertar_suma(Suma)
        print(operaciones1.devolver_suma())
    if Valor_deseado ==2:
        operaciones1.insertar_resta(Resta)
        print(operaciones1.devolver_resta())
    if Valor_deseado ==3:
        operaciones1.insertar_multiplicacion(Multiplicacon)
        print(operaciones1.devolver_multiplicacion())
    if Valor_deseado==4:
        operaciones1.insertar_division(Division)
        print(operaciones1.devolver_division())
    if Valor_deseado==5:
        print("Ha finalizado el programa")
        break

