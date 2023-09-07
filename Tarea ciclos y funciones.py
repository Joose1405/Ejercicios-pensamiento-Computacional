#Ejercicio 1
num = int(input("Ingresa un número: "))
suma = 0
for i in range(num+1):
    suma += i

print("La suma de", num, "a 0 es:",suma)

#Ejercico 2
suma_de_numeros = 0
cantidad_de_numeros = 0

while True:
    a = int(input("Introduce un numero: "))

    if a == 0:
        break #Lo que hace el break es que cierra el ciclo
    else:
        suma_de_numeros += a
        cantidad_de_numeros += 1

if cantidad_de_numeros > 0:
    promedio = suma_de_numeros/cantidad_de_numeros
    print("El promedio de los números que ingresaste es:", promedio)
else:
    print("Error, no se ha introducido ningun número")

#Ejercio 3
n = int(input("Ingrea la cantidad de articulos: "))

lista_compras = []

for i in range(n):
    articulo = input("Ingresa tu articulo #" + str(i+1) + ": ")
    lista_compras.append(articulo)

lista_compras.sort()

print("Tu lista de compras en orden alfabetico es: ")
for articulo in lista_compras:
    print(articulo)

#Ejercicio 4
n = int(input("Ingrese la cantidad de números en la lista: "))

numeros = []

for i in range(n):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

numeros_pares = [num for num in numeros if num % 2 == 0]

print("Números pares en la lista:")
for num in numeros_pares:
    print(num)

#Ejercicio 5
texto = input("Ingresa un texto: ")

vocales = "aeiouAEIOU"

vocales_encontradas = ""

for letra in texto:
    if letra in vocales:
        vocales_encontradas += letra

print("Vocales encontradas:", vocales_encontradas)

#Otra solución del ejercicio 5

#Ejercicio 6
def divisible(num):
    if num % 243 == 0:
        return True
    else:
        return False

num = int(input("Ingrese un número: "))

resultado = divisible(num)

if resultado:
    print(f"{num} es divisible por 243")
else:
    print(f"{num} no es divisible por 243")

#Ejercicio 7
def multiplicación(cadena, n):
    if n <= 0:
        return ""
    else:
        resultado = cadena * n
        return resultado

cadena = input("Ingrese una cadena: ")  
n = int(input("Ingrese un número: ")) 

resultado = multiplicación(cadena, n)

print(f"El resultado de multiplicar '{cadena}' por {n} veces es: {resultado}")

#Otra solucion mas corta para el ejercicio 7 es:


#Ejercico 8
def funcion(a,b,c):
    if(a > 100 or b > 100 or c > 100):
        print(a+b+c)
    else:
        print(a*b*c)

funcion(101,2,3)

#Ejercicio 9
def soloVocales(str):
    vowels = "aeiouAEIOU"
    for c in str:
        if c not in vocales:
            return False
        
    return True

def soloConsonantes():
    vowels = "aeiouAEIOU"
    for c in str:
        if c not in vocales:
            return False
        
    return True

#Solucion del problema 9 en whats

#Solucion del problema 10
'''def esPalindromo():'''

#Challenge 2
n = int(input("Ingresa un número de filas para la pirámide: "))

for i in range(1, n + 1): #El un o es porque inicia en 1 siempre en la piramide
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
