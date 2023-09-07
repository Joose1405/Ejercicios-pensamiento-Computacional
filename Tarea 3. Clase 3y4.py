#Ejercicio 1
def main():
    # Diccionario de c/mes
    days_in_month = {
        "enero": 31,
        "febrero": 28,
        "marzo": 31,
        "abril": 30,
        "mayo": 31,
        "junio": 30,
        "julio": 31,
        "agosto": 31,
        "septiembre": 30,
        "octubre": 31,
        "noviembre": 30,
        "diciembre": 31
    }

    usuario = input("Introduce un mes: ").lower()

    # Verificar si el mes ingresado está en el diccionario
    if usuario in days_in_month:
        days = days_in_month[usuario]
        print(f"El mes de {usuario.capitalize()} tiene {days} días.")
    else:
        print("Mes no válido. Asegúrate de escribir el nombre del mes correctamente.")

#Ejercicio 2
semana = ["nada","lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
a = str(input("Introduce un dia de la semana: "))
print("El día de la semana esta en la posicion número: ", semana.index(a))

#Ejercio 3, se puede mejorar
a = int(input("Introduce un año en números: "))
if a % 4 == 0:
  print("Es un año biciesto")
else:
  print("No es un año biciesto")

#Ejercicio 4
a = int(input("Ingresa un número entero cualquiera: "))
if a%2==0:
    a1="es un numero par,"
elif a%2!=0:
    a1="es un numero impar,"
if a>0:
    b1="positivo"
elif a>0:
    b1="negativo"
if a<100:
    c1="y menor que 100"
elif a>100:
    c1="y mayor que 100"

print(a,a1,b1,c1)

#Ejercicio 5
notas=["DO","RE","MI","FA","SOL","LA","SI"]
notas.remove("MI")
notas.remove("FA")
notas.insert(0,"SI")
notas.insert(0,"SI")
notas.insert(3,"RE")
notas.insert(5,"DO")
notas.insert(6,"SI")
notas.insert(7,"LA")
notas.insert(8,"SOL")
notas.append("SI")
notas.append("LA")
notas.append("LA")

print(notas)

#Ejercio 7
lista = [12,456,2,123]
lista.insert(0,2)
lista.insert(2,123)
lista.pop()
lista.pop()
print(lista)

#Challenge
lado=float(input("Introduzca el valor del lado: "))
diagonal=float(input("Introduzca el valor de la diagonal: "))

if diagonal == (((lado**2) + (lado **2))**0.5):
    resul=(lado*lado + lado*lado)**0.5
    print("Los datos dan un cuadrado y su valor es:", resul)
else:
    print("Es un rectangulo con el valor:",diagonal*lado)

