#Héctor Sebastián Garrido López 1102123
print("Semana 13")

class Circulo:
    def __init__ (self, radio):
        self.radio=radio
    
    def Devolver_perimetro(self):
        return self.radio*3.14*2
    
    def Devolver_Area(self):
        return self.radio*3.14*self.radio

    def Devolver_Volumen(self):
        return (self.radio*self.radio*self.radio*4*3.14)/3
    
radio=float(input("Ingrese el valor del radio:"))
p1=Circulo(radio)
Perimetro= p1.Devolver_perimetro()
Area= p1.Devolver_Area()
Volumen= p1.Devolver_Volumen()
print("El perimetro es:"+str(Perimetro))
print("El Area es:"+str(Area))
print("El Volumen es:"+str(Volumen))

