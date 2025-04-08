# Compreensão de Listas

lista1 = []
for numero in range(1, 11):
  lista1.append(numero)
print(lista1)
print()

lista2 = [numero for numero in range(1,11)]
print(lista2)

print()
lista3 = []
for numero in range(1,11):
  if numero % 2 == 0:
    lista3.append(numero)
print(lista3)

lista4 = [numero for numero in range(1,11) if numero % 2 == 0]
print(lista4)

print()

lista5 = []
for numero in range(1,11):
  if numero % 2 != 0:
    numero = numero ** 2
    lista5.append(numero)
print(lista5)

lista6 = [numero ** 2 for numero in range(1,11) if numero % 2 != 0]

print([(x, y, x + y) for x in range(3) for y in range(3) if (x + y) % 2 == 0])

# EXERCÍCIO
# Com relação ao último exemplo, faça a versão usando o for tradicional com o uso do append
lista7 = []
for x in range(3):
  for y in range(3):
    if (x + y) % 2 == 0:
      lista7.append((x, y, x + y))
print(lista7)
