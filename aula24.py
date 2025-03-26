# EXERCÍCIOS FOR

#  1.Faça um programa que imprima cada elemento da lista [28, 9, 22, -31, -3, -31, 10, 32, 10, 2] usando o for.
lista = [28, 9, 22, -31, -3, -31, 10, 32, 10, 2]
for elemento in lista:
  print(elemento, end=" ")
print()

#  2. Faça um programa que imprima cada elemento da lista [3, 8, 30, 8, 19, -12, -2, -1, -7, -48] usando o for com range.
lista = [3, 8, 30, 8, 19, -12, -2, -1, -7, -48]
for indice in range(len(lista)):
  print(lista[indice], end=" ")

print()

#  3. Crie uma lista com 10 números inteiros e faça um programa que imprima cada elemento da lista usando o for
lista = list(range(1, 11))
for numero in lista:
  print(numero, end=" ")

print()

#  4. Crie uma lista com 10 números inteiros e faça um programa que imprima cada elemento da lista usando o for com range
lista = list(range(10))
for indice in range(10):
  print(lista[indice], end=" ")

print()

# 5. Faça um programa que imprima todos os itens da lista [28, 9, 22, -31, -3, -31, 10, 32, 10, 2] usando while e compare-o com o exercício 1.
lista = [28, 9, 22, -31, -3, -31, 10, 32, 10, 2]
i = 0
while i < len(lista):
  print(lista[i], end=" ")
  i += 1

print()
#  6. Faça um programa que imprima todos os números de 5 a 0 usando o for.

for i in range(5, -1, -1):
  print(i, end=" ")

print()

#  7. Faça um programa que peça para o usuário digitar um número n e imprima uma lista com todos os números de 0 a n-1
n = int(input("Digite um inteiro: "))
lista = list(range(n))
for i in lista:
  print(i, end=" ")

print()
# 8. Faça um programa que imprima o maior número da lista [-8, -6, 3, -1, 7], sem usar o método max(). 
lista = [-8, -6, 3, -1, 7]
print(max(lista))

# 9. Agora, usando o método max(), faça um programa que imprima os três maiores números da lista [2, 9, -5, 2, -8, 4, -9, -5, 4, 1].
lista = [2, 9, -5, 2, -8, 4, -9, -5, 4, 1]
i = 1
while i <= 3:
  maximo = max(lista)
  print(maximo, end=" ")
  lista.remove(maximo)
  i += 1

