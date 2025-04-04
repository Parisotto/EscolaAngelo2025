# TUPLA x LISTA

lista_vazia = []
print(lista_vazia)
lista_vazia.append("Bom dia")
lista_vazia.append("Olá, mundo")
print(lista_vazia)

tupla = ()
print(tupla)
tupla = list(("Ana", "Paula", "Sofia"))
tupla.append("Cristal")
tupla = tuple(tupla)
print(tupla)

print(lista_vazia[0])
print(tupla[3])
