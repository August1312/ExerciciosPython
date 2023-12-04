# Escopo (variáveis locais e globais):

'''
Declare uma variável global e uma função que modifique essa variável global.
Imprima o valor antes e depois da chamada da função.
'''

variavel_global = 'Global'

print(f'\n{variavel_global}')

def modificar_global():
    global variavel_global
    variavel_global = 'Global modificada '
    print(f'\n{variavel_global}') # No interior da funçaõ


modificar_global()
print(f'\n{variavel_global}')

