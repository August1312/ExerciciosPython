# Interpolação básica de strings
# S - string
# D e I - int
# F - float
# x e X - Hexadecimal (adbcdf0123456789)

# Definir variáveis
nome = 'luiz'
preco = 1000.95897643

# Utilizar f-strings para interpolação de strings
variavel = f'{nome} o preço é R$:{preco:.2f}'
print(variavel)

# Utilizar f-strings para interpolação de strings com hexadecimal
hexadecimal = f'O hexadecimal de 1500 é {1500:04x}'
print(hexadecimal)