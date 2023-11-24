# Fatiamento de strings
# 0123456789
# Olá mundo
# -9876543210
# Fatiamento [1:f:p] [::]
# Obs.: a função len retorna a quantidade de caracteres da string.

# Definir a string
variavel = 'hello world'

# Imprimir o quarto caractere a partir do final
print("Quarto caractere a partir do final:", variavel[-4])

# Imprimir o comprimento da string
print("Comprimento da string:", len(variavel))

# Imprimir a substring do índice 4 ao índice 8 (o índice final não é incluído)
print("Substring do índice 4 ao 8:", variavel[4:8])

# Imprimir a string invertida usando fatiamento com passo -1
print("String invertida:", variavel[-1:-12:-1])