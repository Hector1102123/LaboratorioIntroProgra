#Jose Javier Rodas Salazar Y Hector sebastian Garrido
#Laboratorio de programacion, semana 10
#10/10/2023

print ("Semana 10")

def operacion():
    num1 =int(input("Ingrese un numero:"))
    hexa =""
    while num1 > 0:
        resultado = (num1 % 16)
        hexa = str(resultado) + hexa
        num1 = num1//16
    print ("Resultado:"+ hexa)
    
def letras():
    numeros = [10, 11, 12, 13, 14, 15]
    hexa = ["A", "B", "C", "D", "E", "F"]
    if numeros[0] == 10:
        return hexa[0]
    elif numeros[1] == 11:
        return hexa[1]
    elif numeros[2] == 12:
        return hexa[2]
    elif numeros[3] == 13:
        return hexa[3]
    elif numeros[4] == 14:
        return hexa[4]
    elif numeros[5] == 15:
        return hexa[5]


operacion()