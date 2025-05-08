# Fabián Alejandro Salas
# 22.219.807

# Actividad 1
lista = list(range(1, 100, 4))
print(lista)

# Actividad 2
lista = [2, 4, -2, "alumno" , "UTN"]
print(lista[3])

# Actividad 3
lista_vacia = []
for i in range(1, 4):
    dato = input("ingrese una palabra :")
    lista_vacia.append(dato)
print(lista_vacia)

# Actividad 4 
animales = ["perros", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[3] = "oso"
print(animales)

# Actividad 5
# Se crea la lista numeros con los 5 valores
numeros = [8, 15, 3, 22, 7]
# Con max(números) encuentra el máximo valor y lo elimina
numeros.remove(max(numeros))
# Se imprime la lista número sin el máximo valor
print(numeros)

# Actividad 6
lista = list(range(10, 35, 5))
print(lista[0], lista[1])

# Actividad 7
autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1] = "fiat"
autos[2] = "cupé"
print(autos)

# Actividad 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

# Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(compras)
# Item a
compras[2].append("jugo")
print(compras)
# Item b
compras[1][1] = "tallarines"
print(compras)
#Item c
compras[0].remove("pan")
print(compras)

# Actividad 10
# Se crea una lista vacía
lista_anidada = []

# Se agrega en lista en posición 0 el valor 15
lista_anidada.append(15)
print(lista_anidada)

# Se agrega en lista en posición 1 el valor True
lista_anidada.append(True)
print(lista_anidada)

# Se agrega en lista el valor 25.5 la lista anidada
lista_anidada.append([25.5])
print(lista_anidada)

# Se agrega en lista anidada el valor 57.9
lista_anidada[2].append(57.9)
print(lista_anidada)

# Se agrega en lista anidada el valor 30.6
lista_anidada[2].append(30.6)
print(lista_anidada)

# Se agrega en lista en posición 1 el valor True
lista_anidada.append(False)
print(lista_anidada)
