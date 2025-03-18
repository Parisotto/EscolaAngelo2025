# aula21.py

# EXERCÍCIOS DE FIXAÇÃO

# 1.Adicione o número 50 ao final da lista.
lista_numeros = [10, 20, 30, 40]
lista_numeros.append(50)
print(lista_numeros)

# 2. Adicione “laranja” ao índice 1 da lista.
lista_frutas = ["maçã", "banana", "uva"]
lista_frutas.insert(1, "laranja")
print(lista_frutas)

# 3. Remova “cachorro” da lista.
lista_animais = ["cachorro", "gato", "pássaro", "cachorro"]
while "cachorro" in lista_animais:
  lista_animais.remove("cachorro")
print(lista_animais)

# 4. Remova o elemento de índice 2 da lista e mostre o elemento removido.
lista_nomes = ['Alice', 'Bob', 'Charlie', 'David']
# 5. Encontre o índice da primeira ocorrência de ‘azul’ na lista.
lista_cores = ['vermelho', 'azul', 'verde', 'amarelo', 'azul']
# 6. Conte quantas vezes o número 2 aparece na lista.
lista_numeros_repetidos = [1, 2, 3, 2, 4, 2, 5, 2]
# 7. Ordene a lista em ordem crescente.
lista_desordenada = [50, 20, 80, 10, 40]
# 8. Inverta a ordem dos elementos da lista.
lista_invertida = ['maçã', 'banana', 'laranja', 'uva']
