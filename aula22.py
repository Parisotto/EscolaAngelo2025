# EXERCÍCIOS WHILE

#  1. Adivinhação de números:
#  • Criem uma lista com 10 números.
#  • Peçam ao usuário para adivinhar um número da lista.
#  • Usem um loop while para continuar pedindo adivinhações até que o usuário acerte.

numeros = [21, 8, 30, 12, 7, 9, 16, 3, 11, 4]
while True:
  numero = int(input("Digite um numero: "))
  if numero in numeros:
    print("Adivinhou!")
    break

#  2. Contagem regressiva:
#  • Criem uma lista de contagem regressiva de 10 a 1.
#  • Usem um loop while para imprimir cada número da lista

contagem = list(range(1, 11))
i = 9
while i >= 0:
  print(contagem[i])
  i -= 1

# 3. Adição de números:
#  • Criem uma lista vazia para armazenar números.
#  • Peçam ao usuário para fornecer números e os adicionem à lista.
#  • Continuem pedindo números até que o usuário decida parar.

lista1 = []
while True:
  numero = int(input("Digite um número ou 0 para parar: "))
  if numero == 0: 
    break
  lista1.append(numero)

print(lista1)

#  4.Média de notas:
#  • Criem uma lista vazia para armazenar notas.
#  • Peçam ao usuário para fornecer notas e as adicionem à lista.
#  • Calculem e imprimam a média das notas quando o usuário decidir parar

notas = []
while True:
  nota = float(input("Digite uma nota ou 0 para sair: "))
  if nota == 0:
    break
  notas.append(nota)

media = sum(notas) / len(notas)
print(f"Média: {media:.1f}")

# 5.Busca em lista:
#  • Criem uma lista de cinco nomes.
#  • Peçam ao usuário para digitar um nome.
#  • Usem um loop while para verificar se o nome está na lista e informar o resultado.

nomes = ["Edson", "Sandra", "Tamires", "Tales", "Sofia"]
nome = input("Digite um nome: ")
i = 0
while i < len(nomes):
  if nome.capitalize() == nomes[i]:
    msg ="Nome encontrado na lista"
    break
  else:
    msg = "Nome não encontrado"
  i += 1

print(msg)

#  6. Contador de números:
#  • Solicitem ao usuário um número inicial.
#  • Usem um loop while para imprimir os números de 1 até o número fornecido pelo usuário.
#  • Exibam uma mensagem indicando que o loop terminou

numero = int(input("Digite um número: "))
i = 1
while i <= numero:
  print(i, end=" ")
  i += 1
