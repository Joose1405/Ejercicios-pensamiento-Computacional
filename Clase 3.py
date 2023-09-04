# Ejemplo 1
edad = int(input("Escriba su edad: "))
if (edad >= 21):
    print("El usuario es mayor de 21 años")
else:
    print("El usuario es menor de 21 años")

# Ejemplo 2
a = int(input())
b = int(input())
c = int(input())

if (a >= b and a >= c):
    print(a)
elif (b >= a and b >= c):
    print(b)
else:
    print(c)

# Ejemplo 3
a = int(input())
if (a >= 999999999 and a <=10000000000):
    print("Este es un número de telefono")
else:
    print("Este no es un número de telefono")

#Ejemplo 4

#Ejemplo 5
peso = float(input("Escribe tu peso en kg: "))
altura = float(input("Escribe tu altura en m: "))
imc = peso/(altura**2)

if (imc<18.5):
    print("El IMC es inferior al normal")
elif(imc >= 18.5 and imc <= 24.9):
    print("El IMC es normal")
elif(imc >= 25.0 and imc <= 29.9):
    print("El IMC es superior al normal")
else:
    print("El IMC indica obesidad")
