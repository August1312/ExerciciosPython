# Estruturas de Controle (if, else):

'''
Escreva um programa que peça ao usuário para digitar um número e imprima se é par ou ímpar.
'''

numero = int(input('Digite o numero para verificar: '))


# Verifica sé o numero é meenor ou igual a 1
if numero <= -1:
    print(f'O numero e negativo')
elif numero == 1:
    print(f'Numero 1 não pode e primo')
# Verifica se o número é divisível por algum número de 2 ate sua riaz quadrada
for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0: #verifica ser o numero e divisivel por i
        print(f'O Numero {numero} não e primo')
        break
else:
    print(f'O Numero {numero} é Primo:')