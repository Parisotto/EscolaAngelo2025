# EXERCÍCIOS

#  1. Na lista pares = [0, 2, 4, 8]:
#  a) Acrescente o valor 10 ao final da lista.
#  b) Acrescentar o valor 6 na posição 3.
pares = [0, 2, 4, 8]
pares.append(10)
pares.insert(3, 6)
print(pares)

#  2. Na lista ímpares = [1, 3, 3, 5, 7, 9]:
#  a) Remova o valor 3.
#  b) Remova o valor da posição (índice) 4.
#  c) Mostre o valor que será removido da posição (índice)
ímpares = [1, 3, 3, 5, 7, 9]
ímpares.remove(3)
valor_removido = ímpares.pop(4)
print(valor_removido)
print(ímpares)



#  3. Na lista Fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]:
Fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]
#  a) Ordene a lista.
Fibonacci.sort()
print(Fibonacci)
#  b) Coloque em valor reverso a lista Fibonacci.
Fibonacci.reverse()
print(Fibonacci)

#  4. Na lista pi = [3, 1, 4, 1, 5, 9, 2, 6, 5]:
#  a) Busque o elemento que está no índice 5 da lista.
#  b) Imprima o tamanho da lista
#  c) Imprima o valor máximo da lista
#  d) Imprima o valor mínimo da lista
#  e) Imprima apenas o resultado [4, 5]
