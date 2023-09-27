Condicion=True
while Condicion == True:

    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")
    x=input("Ingrese la opcion que desea ejecutar:")
    x2=int(x)
    if x2 == 1:
        numero=int(input("Ingrese valor deseado:"))
        factorial=1
        if numero !=0:
            for i in range(1, numero+1):
                factorial=factorial*i
                print(str(numero)+"="+ str(numero) +"*"+ str(i) +"=" +str(factorial))
    if x2 == 2:
        Numero2=int(input("Ingrese un numero:"))
        a=0
        b=1
        c=1
        while c <= Numero2:
            if c%2 ==1:
                print(a, end="")
                a+=b
            else: 
                print(b, end="")
                b+=a
            c+=1
    if x2==3:
        Condicion=False


     