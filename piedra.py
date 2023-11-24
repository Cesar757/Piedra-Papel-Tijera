import random

print("bienvenidos al juego de piedra papel op tijera")
print("ingrese un valor  piedra=3, tijera=2, papel=1")
n=int(input())
m=random.randint(1,3)
if m==1:
  c="papel"
elif m==2:
  c="tijera"
else:
  c="piedra"

if n==2 and m==2:
  print("empate pc saco "+ c)
else:
  p=n+m
  if p==4:
    if n==1:
      print("ganaste pc saco "+ c)
    else:
      print("perdiste pc saco "+ c)
  else:
    if n>m:
      print("ganaste pc saco "+ c)
    elif n==m:
      print("empate pc saco "+ c)
    else:
      print("perdiste pc saco "+ c)