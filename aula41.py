# Faça uma função que retorne um jogo da mega sena com valores aleatórios não repitidos.
# O usuário deverá dizer quantos números quer jogar, de 6 até 10
# Imprima o resultado solicitado.

from random import randint as rd

def megasena(quantidade = 6):
  numeros = set()
  while True:
    numero = rd(1, 60)
    numeros.add(numero)
    if len(numeros) == quantidade:
      return tuple(numeros)

def jogar():
  while True:
    aposta = input("Quanto números quer joga? Escolha entre 6 a 10: ")
    if aposta.isnumeric():
      aposta = int(aposta)
      if aposta < 6 or aposta > 10:
        print("Quantida inválida, escolha novamente")
      else:
        return megasena(aposta)
    else:
      return megasena(6)

def main():
  jogo = jogar()

  print("\nOs números aletórios solicitados são: ", end='')
  ordenado = sorted(jogo)
  for n in ordenado:
    print(n, end=', ')

  print("\b\b. Boa sorte!\n")

main()