
#import random puede servir para hacer el snake

#Problema 1. Crea una funcion qeu regrese un numero aleatorio
'''import random

def rng(a,b):
   return random.randint(a,b)


for i in range(10):
   randomnumber = rng(2,8)
   print(randomnumber)'''

#Problema 2
import math



def pisodivisones(a,b):
    return math.floor(a/b) #Se declara math.floor porque se llama al calculo dentro de la libreria declarada

#Problema 4
def area(radio):
    area = (math.pi) * (radio **2)

    return area

#print(area(3))

#Solucion del examen del triangulo
def areapentagono(lado, apotema, numlados):
    return lado * numlados * apotema / 2
#En esta libreria "sqrt" significa raiz cuadrada

def calculoradio(area):
    return math.sqrt(area/math.pi)

#31/Agosto - Solución de las tareas
#