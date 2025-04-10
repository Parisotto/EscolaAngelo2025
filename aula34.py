from random import randint

tupla1 = (randint(1,10), randint(1,10), randint(1,10), randint(1,10))
# print(tupla1)

numeros = ()
i = 1
while i <= 6:
  numero = randint(1,100)
  if numero not in numeros:
    numeros += (numero,)
    i += 1

print(numeros)
print(tuple(sorted(numeros)))
print(numeros)
