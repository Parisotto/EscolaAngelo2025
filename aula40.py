from random import randint as rd

print(rd(0,100))

def dados():
  dado1 = rd(1, 6)
  dado2 = rd(1, 6)
  return (dado1, dado2)

jogada = dados()
print(f"O dado 1 deu {jogada[0]} e o dado 2 deu {jogada[1]}")
print(f"A soma dos dois dados é: {jogada[0] + jogada[1]}")
