import os
import random
#
# ACTIVIDAD 1
os.system('cls')
print("Actividad 1")
for i in range(0, 101):
    print(i)
input("Presione ENTER para continuar...")

# ACTIVIDAD 2
os.system('cls')
print("Actividad 2")
n = input("Ingrese un número entero : ")
cont = len(n)

print(f"El número tiene {cont} dígitos")
input("Presione ENTER para continuar...")

# ACTIVIDAD 3
os.system('cls')
print("Actividad 3")
ni = int(input("Ingrese valor entero inicial :"))
nf = int(input("Ingrese valor entero final : "))
suma = 0
for i in range(ni, nf):
    if i > ni:
        print(i)
        suma = suma + i
print(suma)
input("Presione ENTER para continuar...")

# ACTIVIDAD 4
os.system('cls')
print("Actividad 4")

n = int(input("Ingrese un nro entero, (0=salir!): "))
suma = 0
while n != 0:
    suma += n
    n = int(input("Ingrese un nro entero, (0=salir!): "))
print(suma)
input("Presione ENTER para continuar...")

# ACTIVIDAD 5
os.system('cls')
print("Actividad 5")

cont = 1
n_rand = random.randint(0, 9) # Función Random selecciona el número
nro = int(input("Ingrese un nro :"))
while n_rand != nro:
    nro = int(input("Ingrese un nro :"))
    cont += 1
print(f"El número aleatorio fue el {n_rand} y se necesitó {cont} intentos.")
input("Presione ENTER para continuar...")

# ACTIVIDAD 6
os.system('cls')
print("Actividad 6")

for x in range(100, 0, -1):
    if x % 2 == 0:
        print(x)
input("Presione ENTER para continuar...")

# ACTIVIDAD 7
os.system('cls')
print("Actividad 7")

nro = int(input("Ingrese el número entero final positivo :"))
suma = 0
for x in range(0, nro):
    suma += x
print(f"La suma de todos los números comprendidos entre (0,{nro}) es {suma}")
input("Presione ENTER para continuar...")

# ACTIVIDAD 8
os.system('cls')
print("Actividad 8")
max = int(input("Cantidad máxima de números que desea ingresar :"))
cont = 1
cpar = 0
cimp = 0
cneg = 0
cpos = 0

while cont <= max:
    nro = int(input(f"Nro {cont} : "))
    cont += 1
    if (nro % 2 == 0) and (nro != 0):
        cpar += 1
    else:
        cimp += 1
    if nro > 0:
        cpos += 1
    elif nro < 0:
        cneg += 1      
print(f"Par={cpar} Impar={cimp} Positivo={cpos} Negativos={cneg} Total={max}")
input("Presione ENTER para continuar...")

# ACTIVIDAD 9
os.system('cls')
print("Actividad 9")

max = int(input("Cantidad máxima de números que desea ingresar :"))
cont = 1
suma = 0

while cont <= max:
    nro = int(input(f"N° {cont}:"))
    suma = suma + nro
    cont += 1
media = suma/max
print(f"La suma de números ingresados es {suma} y su promedio es {media}")
input("Presione ENTER para continuar...")

# ACTIVIDAD 10
os.system('cls')
print("Actividad 10")

n = input("Ingrese número para invertir:")
nro_invertido = ""

for i in n:
    nro_invertido = i + nro_invertido
print("Número invertido :" + nro_invertido) 

input("Presione ENTER para continuar...")
