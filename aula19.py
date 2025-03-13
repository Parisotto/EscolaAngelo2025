nomes = ["Ana", "Paula", "Maria", "Sofia", "Fernanda", "Sofia"]

print(f"A primeira ocorrência de Sofia é no índice: {nomes.index("Sofia")}")

print(f"Sofia aparece {nomes.count("Sofia")} vezes na lista")

nomes.sort()
print(nomes)

nomes.reverse()
print(nomes)

copiaNomes = nomes.copy()
print(f"Nomes copiados: {copiaNomes}")
