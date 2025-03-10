# 1. Faça um programa que peça a idade do usuário e imprima se ele é maior ou menor de 18 anos.

idade = int(input("Digite sua idade: "))

if idade >= 18:
  print("É de maior!")
else:
  print("É de menor!")

# 2. Faça um programa que peça um número e mostre se ele é positivo ou negativo.

numero = int(input("Digite um número inteiro: "))

if numero >= 0:
  print("O número é positivo!")
else:
  pirnt("O número é negativo!")

# 3. Faça um programa que, dado um número digitado, mostre se ele é par ou ímpar.

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
  print("O número é par.")
else:
  print("O número é impar.")


# 4 Faça um programa que peça dois números e mostre o maior deles.

n1 = int(input("Digite um inteiro: "))
n2 = int(input("Digite outro inteiro: "))

if n1 > n2:
  print(n1)
else:
  print(n2)

# 5. Faça um programa que leia a validade das informações:
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou outro;

idade = int(input("Digite a idade maior que 0 menor 150: "))
if idade > 0 and idade < 150:
  print("idade válida")
else:
  prin("idade inválida")

salario = int(input("Digite o salário: R$ "))
if salario > 0:
  print(f"O salário é R$ {salario}")
else:
  print("Salário inválido")

sexo = input("Digite o sexo [M, F, outro]: ")
if sexo == "M":
  print("Sexo masculino")
elif sexo == "F":
  print("Sexo feminino.")
elif sexo == "outro":
  print("Sexo outro")
else:
  print("Sexo inválido")


