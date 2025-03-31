#  Você está construindo um sistema de gerenciamento de contatos. Crie um programa que realize as seguintes tarefas:

#  a) Peça ao usuário para digitar seu nome completo.
nome_completo = input("Digite seu nome completo: ")

#  b) Concatene “Olá,” com o nome fornecido e exiba o resultado.
nome_completo = "Olá, " + nome_completo
print(nome_completo)

#  c) Conte quantos caracteres existem no nome completo digitado e exiba o resultado.
caracteres = len(nome_completo)
print(f"Seu nome completo tem {caracteres} caracteres.")

#  d) Peça ao usuário para digitar um sobrenome para procurar na string do nome completo.
sobrenome = input("Digite um sobrenome para ser procurado no seu nome completo: ")

#  e) Verifique se o sobrenome fornecido está presente no nome completo e exiba uma mensagem apropriada.
if sobrenome in nome_completo:
  print(f'O sobrenome {sobrenome} está presente no nome completo')
else:
  print(f"O sobrenome {sobrenome} NÃO está presente no nome completo.")

#  f) Exiba o nome completo em letras maiúsculas.
print("Seu nome completo em letras maiúsculas é", nome_completo.upper())

#  g) Substitua todas as ocorrências da vogal “a” na string do nome completo pelo caractere ‘4’ e exiba o resultado
nome_completo = nome_completo.replace("a", "4")
print("Nome completo com 'a' substituído por '4': ", nome_completo)
