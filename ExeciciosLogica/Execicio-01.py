# Tipos de Dados (Listas):
'''
Escreva um programa que declare duas variáveis, 
atribua valores a elas e imprima a soma desses valores.
'''
import numpy as np


variavel_1 = [2]
variavel_2 = [8]

# Garante que ambas as listas têm o mesmo comprimento
assert len(variavel_1) == len(variavel_2)

# Realiza a adição elemento a elemento
soma = [v1 + v2 for v1, v2 in zip(variavel_1, variavel_2)]

print(f'A soma da Variavel 1 com a Variavel 2 é: {soma}')


# Utilizando numpy

#converte as lista em arrys do Numpy
Array_1 = np.array(variavel_1)
Array_2 = np.asarray(variavel_2)

# Realiza a adição elemento a elemento
soma1 = Array_1 + Array_2 

print(f'\n A soma da Variavel 1 com a Variável 2 é: {soma1.tolist()}')


# Loop para somar 

# Inicializa uma lista fazia para armazenar a soma 
soma3 = []

for v1, v2 in zip(variavel_1, variavel_2):
    soma3.append(v1 + v2)
    
print(f'\n A soma da Variavel 1 com a Variavel 2 é: {soma3}')