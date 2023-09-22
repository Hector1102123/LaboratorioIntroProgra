print("Ejercicio 3 Jerarquia de operaciones")
print("Tomar en cuenta que ningún valor puede ser 0")
print("Ingrese valor a")
a=input()
print("Ingrese el valor b")
b=input()
print("Ingrese el valor c")
c=input()
a2=int(a)
if a2 ==0:
      print("Error, a no puede tomar el valor de 0, cambie el valor.")
      Condicion=False
b2=int(b)
if b2==0:
      print("Error, b no puede tomrar el valor de 0, cambie el valor." )
      Condicion=False
c2=int(c)
if c2==0: 
      print("Error, c no puede tomar el valor de 0, cambie el valor.")
      Condicion=False
operacion1=a2*b2+c2
operacion2=a2*(b2+c2)
operacion3=a2/(b2*c2)
operacion4=(3*a2+2*b2)/c2**2
operacion5=-(b2)+(b2**2-(4*a2*c2))**0.5/(2*a2)
operacion6=-(b2)-(b2**2-(4*a2*c2))**0.5/(2*a2)
verificar=b2**2-(4*a2*c2)
print("si desea realizar la operación 1 marque op1, si desea realizar la operación 2 marque op2, si desea realizar la operación 3 marque op3, si desea realizar la operación 4 marque op4, si desea realizar la operación 5 marque op5 (nota para realizar la op5 debe realizar primero verificar oprimiendo ver) y si no desea continuar marque No.")
Condicion=True
while Condicion == True:
    continuar=input("Ingrese la operacion que desea:")
    if continuar=="op1":
        print(operacion1)
    elif continuar=="op2":
        print(operacion2)
    elif continuar=="op3":
        print(operacion3)
    elif continuar=="op4":
        print(operacion4)
    if continuar=="ver":
         print(verificar)
         if verificar >=0:
             print("Si se puede realizar operación número 5, marque op5")
         else: 
                       print("No es posible realizar la operación número 5, por favor cambiar el valor de a, b y c.")
                       Condicion=False
    if continuar=="op5":
            print(operacion5)
            if continuar =="op5":
                 print(operacion6)
    if continuar=="No":
         Condicion=False