#Ejercicio 12
'''lado=float(input())
area= (lado*lado)/2

print(area)'''

#11. "and" es un comando que se utiliza para decir que si una condicion se cumple Y otra igual, entonces el valor es verdadero
#"or" es un comando que se utiliza para decir que, si entre dos condiciones una se cumple, entonces el valor es verdadero
#"not" es un comando que se utiliza para decir que si una condicion es diferente a otra condicione entonces el valor es verdadero

#10. Una variable es un dato que escribimos en el codigo y en la cual iremos interactuando y/o operando con esta para conseguir un resultado

#9. Los tipos de datos que existen en Python son los "strings", los "float", los "bolean" y los "enteros (int)"

#8. Un sting es un tipo de dato de texto

#7. len es la instrucción para saber el tamaño de un String o una Lista.

#6. "remove" e "insert" son dos instrucciones que se pueden usar con listas

#Ejercico 2
'''a = int(input("Precios de los vuelos del año pasado: "))
b = int(8000)

dif = b-a
porc_incre = (100*dif)/a

print("La diferencia de precio es de:", dif, "y en comparacion incremento un:", porc_incre)'''

#Ejercicio 3
'''a = int(input("Introduce un número: "))

if a%2 == 0:
    print(a,"Es un número par")
else:
    print(a,"Es un número impar")'''

#Ejercicio 4
'''libros = ["Biblia","Coran","Principito","El diario de Greg","Programación en Python","Algoritmos avanzados","Algebra de Baldor"]

libros.insert(0,"El diario de Munganita")
libros.insert(0,"Pequeño cerdo capitalista")
libros.insert(0,"El diario de Greg 2")
libros.insert(0,"Nose que poner aqui")
libros.insert(0,"Harry Potter")
libros.pop(9)
libros.pop(10)
libros.pop(5)
libros.pop(6)
libros.insert(5,"CORAN")
libros.insert(6,"BIBLIA")

print(libros)'''

#Ejercicio 1
'''a=int(input("Inserta el amperaje: "))
b=int(input("Inserta el valor de la resistencia: "))

v = a*b

print("El valor del voltaje es:", v)'''

#Ejercicio 5
lado1 = int(input("Escribre el valor de un lado: "))
apotema1 = float(input("Escribe el valor del apotema: "))

pregunta = str(input("La figura es el hexagono: (SI/NO)"))

if pregunta == "SI":
    area1 = (1/2)*((6*lado1)*(apotema1))
else:
    lado2 = int(input("Escribre el valor del lado del pentagono: "))
    apotema2 = float(input("Escribe el valor del apotema del pentagono: "))
    area2 = (1/2)*((5*lado2)*(apotema2))

if area1 > area2:
    print("El valor del area del herxagono es:", area1, "y es el que mas conviene.")
