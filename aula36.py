# Colocar em uma lista uma outra lista só de pares e outra lista só de impares
from random import randint as r

valores = [[],[]]

for x in range(15):
  valor = r(1,100)
  if valor % 2 == 0:
    indice = 0
  else:
    indice = 1

  if valor not in valores[indice]:
    valores[indice].append(valor)

print(valores)
print("Pares: ", sorted(valores[0]))
print("Ímpares: ", sorted(valores[1]))
