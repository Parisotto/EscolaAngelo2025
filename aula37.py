from random import randint as r

matriz = [[0,0,0],[0,0,0],[0,0,0]]

# Adicionar inteiros aleatórios a cada item da matriz
# somar os valores pares
# somar os valores da terceira coluna
# o maior valor da segunda linha

soma = coluna3 = maior = 0
for linha in range(3):
  for coluna in range(3):
    numero = r(1,100)
    matriz[linha][coluna] = numero
    if numero % 2 == 0:
      soma += numero
    if coluna == 2:
      coluna3 += numero
    if linha == 1 and numero > maior:
      maior = numero
    print(f"[{matriz[linha][coluna]:^4}]", end="")

  print()

print("A soma dos pares é: ", soma)
print("A soma da terceira coluna é: ", coluna3)
print("O maior valor da segunda linha é: ", maior)
