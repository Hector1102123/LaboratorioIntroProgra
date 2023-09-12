print("Ejercicio 2")
v1=input("Ingrese nùmero de dìa")
xnum=int(v1)
print(type(xnum))
if xnum==1:
    print("Lunes")
if xnum==2:
    print("Martes")
if xnum==3:
    print("Miercoles")
if xnum==4:
    print("Jueves")
if xnum==5:
    print("Viernes")
if xnum==6:
    print("Sabado")
if xnum==7:
    print("Domingo")
if xnum<1:
    print("No existee, pues debe estar entre 1 y 7")
if xnum>7:
    print("No existe debe ser menor que 7")