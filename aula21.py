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

