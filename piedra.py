import random

print("bienvenidos al juego de piedra papel op tijera")
print("ingrese un valor  piedra=3, tijera=2, papel=1")
n=input()
m=random.randint(1,3)
if m==1:
  c="papel"
elif m==2:
  c="tijera"
else:
  c="piedra"
print(c)