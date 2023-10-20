#Héctor Sebastián Garrido López
#1102123
print("Tarea Semana 11")

Cadena_de_caracteres=input("Ingrese una cadena de caracteres, con la condición que unicamente puede ingresar el número 1 y el número 0:")
ceros=str(Cadena_de_caracteres.count("0"))
unos=str(Cadena_de_caracteres.count("1"))
caracteres=len(str(Cadena_de_caracteres))
Resto_de_caracteres=caracteres-int(ceros)-int(unos)
print("Cadena:"+Cadena_de_caracteres)
print("El numero total de caracteres es:"+str(caracteres))
print("Cantidad de 0:"+str(Cadena_de_caracteres.count("0")))
print("Cantidad de 1:"+str(Cadena_de_caracteres.count("1")))
print("La cantidad del resto de caracteres es:"+str(Resto_de_caracteres))
