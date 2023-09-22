print("Ejercicio 1 Operaciones Aritmeticas")
print("Ingrese valor 1")
x=input()
print("Ingrese valor 2")
y=input()
x2=int(x)
y2=int(y)
suma=x2+y2
resta=x2-y2
multiplicacion=x2*y2
division=x2/y2
modulo=x2%y2
Exponente=x2**y2
Cociente=x2//y2
print("Si desea realizar una suma marque s, si desea realizar una resta marque r, si desea realizar una division marque d, si desea realizar una multiplicacion marque m, si desea realizar modulo marque mo, si desea realizar exponente marque e y si desea el cociente marque c y si no desea continuar marque N.")
condicion=True
while condicion==True:
    continuar= input("ingrese la letra de operacion que desea:")
    if continuar =="s":
        print(x+"+"+y+"="+str(suma))
    elif continuar =="r":
        print(x+"-"+y+"="+str(resta))
    elif continuar == "d":
        print(x+"/"+y+"="+str(division))
    elif continuar == "m":
        print(x+"*"+y+"="+str(multiplicacion))
    elif continuar == "mo":
        print(x+"%"+y+"="+str(modulo))
    elif continuar == "e":
        print(x+"**"+y+"="+str(Exponente))
    elif continuar == "c":
        print(x+"//"+y+"="+str(Cociente))
    elif continuar == "N":
        condicion= False

