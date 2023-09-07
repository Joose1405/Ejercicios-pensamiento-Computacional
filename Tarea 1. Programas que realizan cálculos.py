#Ejercicio 1
a = int(input())
b = int(input())
print(a == (b*20))

#Ejercicio 2
a = int(input())
b = int(input())
c = int(input())
print(int((a*b*c)/(a+b+c)))

#Ejercicio 3
a = int(input())
b = int(input())
c = int(input())
print(a<b<c)

#Ejercicio 4
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print((a and b and c and d) <0)
#print(a <0 and b <0 and c <0 and d <0) Si se podia asi igual ;D

#Ejercicio 5
a = int(input())
if a % 2 == 0:
  print(True)
else:
  print(False)

#Ejercicio 6
a = int(input())
b = int(input())
c = int(input())
print((a<b) and (b!=c))

#Ejercicio 7
a = int(input())
b = int(input())
c = int(input())
print((a==b) or (a>(b+3)))

#Ejercicio 8
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
print((a+b+c+d+e+f+g+h)/8)

#Ejercicio 9
a = str(input())
b = str(input())
c = str(input())
d = str(input())
print(a, b, c, d)

#Ejercicio 10 SANDIA CHALLENGE
peso_sandia = int(input())
resultado = peso_sandia / 2
if resultado % 2 == 0:
  print(True)
else:
  print(False)
#De este tengo duda