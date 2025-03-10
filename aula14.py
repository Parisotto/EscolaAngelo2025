x = 1
while x <= 5:
  #print(x)
  x += 1

while True:
  #print(x)
  x = x + 2
  if x > 1000:
    break

linha = 1
while linha <= 5:
  coluna = 1
  while coluna <= linha:
    print("*", end=" ")
    coluna = coluna + 1

  print()
  linha = linha + 1

