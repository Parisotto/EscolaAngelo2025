# FUNÇÕES

# len() => tamanho
lista = [1,2,3,4,5,6,7,8,9,0,7]
print(len(lista))
print(lista[len(lista)-1])

# max() => valor máximomaior valor
print(max(lista))
# min() => menor valor
print(min(lista))
# sum() => soma todos os elementos numéricos
print(sum(lista))

tamanho = len(lista)
print(tamanho)

lista.insert(2, 21)
print(lista)

print()
while 7 in lista:
  lista.remove(7)
  print(lista)
print("Acabou")