# Colocando número em ordem em uma lista sem usar sort() ou sorted()

lista = []
while True:
  valor = input("Digite um número ou s para sair: ")
  if valor.lower() == 's': break
  if valor.isnumeric():
    valor = int(valor)
    if valor in lista:
      continue
    if len(lista) == 0 or valor > lista[-1]:
      lista.append(valor)
    else:
      indice = 0
      while indice < len(lista):
        if valor <= lista[indice]:
          lista.insert(indice, valor)
          break
        indice += 1

print(lista)
