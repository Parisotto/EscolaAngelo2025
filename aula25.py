# STRINGs

texto = "Ciência de Dados!"

print(texto[11])
print(texto[0:7])
print(texto[11:17])
print(texto[-1])
print(texto[-6])
print(texto[-6:-1])
print(texto[7:11])

achei = " de " in texto
print(achei)

print(texto[:-1])
print(texto)
print(texto[:])

# texto[16] = "?" # não é possível
texto_temporario = texto[:-1] + "?"
texto = texto_temporario[:]

print(texto)
print(texto_temporario)


str1 = "Olá"
str2 = "mundo"

print(str1 + str2)

str3 = str1 + ", " + str2 + "!"
print(str3)

print(f"O tamanho da string {texto} é {len(texto)} caracteres")

maiusculo = texto.upper()
print(texto.upper())
print(maiusculo)
print(texto)

minusculo = texto.lower()
print(minusculo)
print(texto)

texto = texto.upper()
print(texto)

texto = texto.capitalize()
print(texto)

texto = texto.title()
print(texto)

texto = texto.replace(" De ", " de ")
print(texto)

texto = "Aula de " + texto
print(texto)

texto = texto.replace("Aula de ", "Curso ")
print(texto)

texto = texto.replace("Curso ","Curso de ")
print(texto)
