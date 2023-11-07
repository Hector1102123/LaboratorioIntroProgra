#Héctor Sebastián Garrido López 1102123
print("Laboratorio 14")

class Automovil:
    def __init__ (self):
        self.modelo=2024
        self.precio=80000
        self.marca="Toyota"
        self.disponible=False
        self.cambiodolar=7.28
        self.descuento=2000
        self.precio_final=78000

    def devolver_modelo(self):
        return self.modelo
    def devolver_precio(self):
        return self.precio
    def devolver_marca(self):
        return self.marca
    def devolver_disponible(self):
        return self.disponible
    def devolver_cambiodolar(self):
        return self.precio*7.28
    def devolver_descuento(self):
        return self.descuento
    def devolver_precio_final(self):
        return self.precio_final

p1=Automovil()
Modelo=p1.devolver_modelo()
Precio=p1.devolver_precio()
Marca=p1.devolver_marca()
Disponibilidad=p1.devolver_disponible()
Cambio_dolar=p1.devolver_cambiodolar()
Descuento=p1.devolver_descuento()
Precio_dolar=p1.devolver_cambiodolar()
Precio_final=p1.devolver_precio_final()
print("Marca:"+ str(Marca))
print("Modelo:"+str(Modelo))
print("El precio de venta es de:"+str(Precio)+"Q")
print("El precio en dolares es:"+str(Precio_dolar)+"$")
if Disponibilidad==False:
    print(True)
    print("se encuentra disponible")
print("El precio final ya con descuento es:"+str(Precio_final))


