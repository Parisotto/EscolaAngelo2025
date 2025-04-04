# Conjunto (set) x Lista

lista = []
tupla = ()
conjunto = {}

lista.append("item")
tupla # não tem como adicionar
conjunto[0] = "item"

print(conjunto)

for i in conjunto:
  print(i)

print(conjunto[0])

conjunto = set(range(0, 11))
print(conjunto)

# i = 0
# while i < len(conjunto):
#   print(conjunto[i])
#   i += 1

for item in conjunto:
  print(item)


