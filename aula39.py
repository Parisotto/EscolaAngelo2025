import random 

print(random.randint(4, 9))

print("Olá")

def mensagem():
  print("Olá, mundo!")

mensagem()

def mensagem(texto):
  print(texto)

mensagem("Eu sou a lenda!")

def mensagem(texto, numero):
  print(texto, numero)

def soma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado

print(soma(7, 9))

def dobrar(lista):
  indice = 0
  while indice < len(lista):
    lista[indice] *= 2
    indice += 1

valores = [7, 2, 9, 3, 0, 1]
print(valores)
dobrar(valores)
print(valores)
