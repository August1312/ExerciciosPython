# Formatação básica de strings
# s - strings
# d - int
# f - float
# .<numero de dígitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - esquerda
# < - direita
# ^ - centro
# sinal - + ou -
# ex. 0>-100, .1f
# Conversion flags - ir !s !a

# Definir uma variável de exemplo
variavel = 'abc'

# Imprimir a string simples
print(f'String simples: {variavel}')

# Imprimir a string alinhada à direita com preenchimento de ponto de exclamação
print(f'String alinhada à direita: {variavel:!>10}')

# Imprimir a string alinhada à esquerda com preenchimento de cerquilha e ponto no final
print(f'String alinhada à esquerda: {variavel:#<10}.')

# Imprimir a string centralizada com preenchimento de "&"
print(f'String centralizada: {variavel:&^10}')

# Imprimir a string centralizada com preenchimento de "$"
print(f'String centralizada: {variavel:$^10}')

# Imprimir um número float com separadores de milhares e 3 casas decimais
print(f'Número float com separadores: {100000.5544535634:,.3f}')

# Imprimir um número float com separadores de milhares e 3 casas decimais (repetição para fins de exemplo)
print(f'Número float com separadores (repetição): {100000.5544535634:,.3f}')

# Imprimir o valor hexadecimal de 1500 com 8 dígitos, preenchendo zeros à esquerda
print(f'O hexadecimal de 1500 é: {1500:08x}')

# Imprimir a representação de "variavel" usando !r (representação)
print(f'Representação da variável: {variavel!r}')
