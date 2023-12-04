 #Tipos de Dados (Listas):
'''
Crie uma lista de números e escreva um programa que calcule e imprima a média desses números.

'''

LISTA_01 = [1,2,3,4,4,5,6,7,7,8,9,9,10]

# Calcula o número total de elementos na lista
soma = sum(LISTA_01)

# Calcula o número total de elementos na lista
numero_elementos = len(LISTA_01)

# Calcula a média 
media = soma /numero_elementos

print(f'A média dos números na lista é: {media: .2f}')