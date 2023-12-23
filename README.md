def rondas(rondas=5):
     if rondas<=1:
        print("No te quedan más rondas.")
     else:
        print(f"Te quedan {rondas-1} rondas.")
# en esta parte agregue rondas al juego, 5 rondas para ser exacto

print("Bienvenidos al juego de piedra papel o tijera")
print("Mi nombre es Cesar y soy un Boot")
print("Quiero retarte a un juego de Piedra, Tijera o Papel, en el que el mejor de 5 ganará")
print("Seras capaz de ganarme?")
print("Empezemos.... selecciona  piedra=3, tijera=2, papel=1")
# print imprimira mensajes de bienvenida, anunciando el juego, y su modalidad, tambien dando a conocer las opciones de juego

import random


n=int(input()) 
# la letra n representa al player 
m=random.randint(1,3)
# la letra m representa al boot Cesar
if m==1:
  c="papel"
elif m==2:
  c="tijera"
else:
  c="piedra"
# en esta parte del sesarrollo del software determinamos la seleccion del boot Cesar
if n==2 and m==2:
  print("empate el boot Cesar saco "+ c)
else:
  p=n+m
  if p==4:
    if n==1:
      print("ganaste el boot Cesar saco "+ c)
    else:
      print("perdiste el boot Cesar saco "+ c)
  else:
    if n>m:
      print("ganaste el boot Cesar saco "+ c)
    elif n==m:
      print("empate el boot Cesar saco "+ c)
    else:
      print("perdiste el boot Cesar saco "+ c)
# aqui podemos verificar el resultado mediante if elif else ya que estos comandos actuan como preguntas las cuales determinan los resultados 

rondas()
# como dije en un inicio se agregaron ronas al juego, podemos saber en que ronda nos encontramos 
n=int(input())
m=random.randint(1,3)
if m==1:
  c="papel"
elif m==2:
  c="tijera"
else:
  c="piedra"

if n==2 and m==2:
  print("empate el boot Cesar saco "+ c)
else:
  p=n+m
  if p==4:
    if n==1:
      print("ganaste el boot Cesar saco "+ c)
    else:
      print("perdiste el boot Cesar saco "+ c)
  else:
    if n>m:
      print("ganaste el boot Cesar saco "+ c)
    elif n==m:
      print("empate el boot Cesar saco "+ c)
    else:
      print("perdiste el boot Cesar saco "+ c)
rondas(rondas=4)
#desde aqui la codificaion se repite ya que son 5 rondas
n=int(input())
m=random.randint(1,3)
if m==1:
  c="papel"
elif m==2:
  c="tijera"
else:
  c="piedra"

if n==2 and m==2:
  print("empate el boot Cesar saco "+ c)
else:
  p=n+m
  if p==4:
    if n==1:
      print("ganaste el boot Cesar saco "+ c)
    else:
      print("perdiste el boot Cesar saco "+ c)
  else:
    if n>m:
      print("ganaste el boot Cesar saco "+ c)
    elif n==m:
      print("empate el boot Cesar saco "+ c)
    else:
      print("perdiste el boot Cesar saco "+ c)
rondas(rondas=3)

n=int(input())
m=random.randint(1,3)
if m==1:
  c="papel"
elif m==2:
  c="tijera"
else:
  c="piedra"

if n==2 and m==2:
  print("empate el boot Cesar saco "+ c)
else:
  p=n+m
  if p==4:
    if n==1:
      print("ganaste el boot Cesar saco "+ c)
    else:
      print("perdiste el boot Cesar saco "+ c)
  else:
    if n>m:
      print("ganaste el boot Cesar saco "+ c)
    elif n==m:
      print("empate pel boot Cesar saco "+ c)
    else:
      print("perdiste el boot Cesar saco "+ c)
rondas(rondas=2)

n=int(input())
m=random.randint(1,3)
if m==1:
  c="papel"
elif m==2:
  c="tijera"
else:
  c="piedra"

if n==2 and m==2:
  print("empate el boot Cesar saco "+ c)
else:
  p=n+m
  if p==4:
    if n==1:
      print("ganaste el boot Cesar saco "+ c)
    else:
      print("perdiste el boot Cesar saco "+ c)
  else:
    if n>m:
      print("ganaste el boot Cesar saco "+ c)
    elif n==m:
      print("empate el boot Cesar saco "+ c)
    else:
      print("perdiste el boot Cesar saco "+ c)
#una vez finalizado el juego el mismo programa informa que el juego a terminado y podemos ver los resultados.

      r=("""el juego ha finalizado ya tenemos los resultados""")
print(r)
print("No te quedan más rondas.")
