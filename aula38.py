# EXERCÍCIO MATRIZ 3x3 (Tipo Jogo da Velha)

# Crie uma matriz 3x3 com cada elemento prenchido com valores sequenciais de 1 a 9
matriz = [[1,2,3],[4,5,6],[7,8,9]]
marcador = "X"

while True:
  # Imprima cada linha da matriz em um linha diferente.
  print()
  for linha in matriz:
    for valor in linha:
      print(f'[{valor:^3}]', end="")
    print()

  # Solicite ao usário escolher uma das nove posições digitando o número correspondente
  escolha = input("Digite um dos números da matriz ainda disponíveis: ")

  # Verifique se o usuário digitou mesmo um número válido e dentro do intervalo de 1 a 9
  if escolha.isnumeric():
    escolha = int(escolha)
    if escolha >=1 and escolha <= 9:
  # Substitua o valor escolhido por X (letra X maiúscula) ou por O (letra O maiúscula) alternadamente começando por X
      feito = False
      for linha in range(3):
        for coluna in range(3):
          if matriz[linha][coluna] == escolha:
            matriz[linha][coluna] = marcador
            feito =True
            if marcador == "X":
              marcador = "O"
            else:
              marcador = "X"
  # Se a casa escolhida pelo usuário já tiver sido preenchida antes por X ou O, imprima uma mensagem informando e solicite novamente outra opção válida.
      if feito == False:
        print("\nEsta dasa já foi escolhida! Escolha outra opção válida!")
  # Quando todas as 9 casas da matriz tiver sido preenchidas, avise o usuário e termine o programa.
  continuar = False
  for linha in matriz:
    for valor in linha:
      if valor in list(range(1,10)):
        continuar = True
        break
    if continuar:
      break

  print()
  if continuar == False:
    for linha in matriz:
      for valor in linha:
        print(f'[{valor:^3}]', end="")
      print()
    print("Todas as casas já foram preenchidas!")
    print("Fim do program!\n")
    break