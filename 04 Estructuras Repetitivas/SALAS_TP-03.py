import os
from statistics import mode, median, mean
import random

# ACTIVIDAD 1
os.system('cls')

edad = int(input("Ingrese su edad, por favor: "))
if edad > 18:
    print("Es mayor de 18.")
elif edad > 65:
    print("Es mayor a 65")
else:
    print("Es menor a 18")

input("Presione una tecla para continuar...")


# ACTIVIDAD 2
os.system('cls')
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")
input("Presione una tecla para continuar...")

# ACTIVIDAD 3
os.system('cls')
nro = int(input("Ingrese un número entero :"))
if nro % 2 == 0:
    print(f"{nro} es par.")
else:
    print(f"{nro} es impar.")

input("Presione una tecla para continuar...")

# ACTIVIDAD 4
os.system('cls')
edad = int(input("Ingrese su edad :"))
if (edad >= 12) and (edad < 18):
    print("Adolescente.")
elif (edad >= 18) and (edad < 30):
    print("Adulto/a joven.")
elif (edad >= 30):
    print("Adulto/a.")
else:
    print("Niño/a")

input("Presione una tecla para continuar...")

# ACTIVIDAD 5
os.system('cls')
psw = len(input("Ingrese contraseña : "))
if (psw >= 8) and (psw <= 12):
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
  
input("Presione una tecla para continuar...")

# ACTIVIDAD 6
os.system('cls')

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

if (mean(numeros_aleatorios) > median(numeros_aleatorios)):
    if (median(numeros_aleatorios) > mode(numeros_aleatorios)):
        print("Sesgo positivo o a la derecha.")
elif (mean(numeros_aleatorios) < median(numeros_aleatorios)):
    if (median(numeros_aleatorios) < mode(numeros_aleatorios)):
        print("Sesgo negativo o a la izquierda.")
elif (mean(numeros_aleatorios) == median(numeros_aleatorios)):
    if (median(numeros_aleatorios) == mode(numeros_aleatorios)):
        print("Sin sesgo.")
else:
    pass

input("Presione una tecla para continuar...")

# ACTIVIDAD 7
os.system('cls')
cadena = input("Ingrese una frase o palabra :")
cantidad_de_letras = int(len(cadena))

if (cadena[cantidad_de_letras-1] == "a"):
    print(cadena + "!") 
elif (cadena[cantidad_de_letras-1] == "e"):
    print(cadena + "!")
elif (cadena[cantidad_de_letras-1] == "i"):
    print(cadena + "!")
elif (cadena[cantidad_de_letras-1] == "o"):
    print(cadena + "!") 
elif (cadena[cantidad_de_letras-1] == "u"):
    print(cadena + "!")
else:
    print(cadena)
     
input("Presione una tecla para continuar...")

# ACTIVIDAD 8
os.system('cls')
nombre = input("Ingrese su nombre, por favor :")
print("1 - Nombre en mayúsculas.")
print("2 - Nombre en minúsculas.")
print("3 - Nombre en primera en mayúsculas.")
opcion = int(input("Ingrese una opción (1,2,3) :"))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    pass

input("Presione una tecla para continuar...")


# ACTIVIDAD 9
os.system('cls')
escala = int(input("Ingrese escala de Ritcher registrada :"))
if escala < 3:
    print("Muy leve(imperceptible)")
elif (escala >= 3) and (escala < 4):
    print("Leve(ligeramente perceptible)")
elif (escala >= 4) and (escala < 5):
    print("Moderado (Sentido por personas, pero gralmente no causa daños.)")
elif (escala >= 5) and (escala < 6):
    print("Fuerte (Puede causar daños en estructuras débiles.)")
elif (escala >= 6) and (escala < 7):
    print("Muy fuerte.(puede causar daños significativos.)")
elif escala >= 7:
    print("Extremo (puede causar graves daños a gran escala.)")
else:
    pass

input("Presione una tecla para continuar...")


# ACTIVIDAD 10
os.system('cls')
h = input("Ingrese el hemisferio (N/S):").upper()
dia = int(input("Ingrese el día :"))
mes = int(input("Ingres el mes :"))
if (mes >= 12 and dia >= 21) or ((mes >= 1 and mes <= 3) and dia <= 20):
    if h == "N":
        print("Invierno")
    else:
        print("Verano")
elif (mes >= 3 and mes <= 6) and (dia >= 21 or dia <= 20):
    if h == "N":
        print("Primavera")
    else:
        print("Otoño")
elif (mes >= 6 and mes <= 9) and (dia >= 21 or dia <= 20):
    if h == "N":
        print("Verano")
    else:
        print("Invierno")
elif (mes >= 9 and mes <= 12) and (dia >= 21 or dia <= 20):
    if h == "N":
        print("Otoño")
    else:
        print("Primavera")
else:
    pass

input("Presione una tecla para continuar...")