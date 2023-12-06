# Exercício 5: Estruturas de Controle (elif):

'''
Escreva um programa que peça ao usuário para digitar um número e, em seguida,
classifique-o como positivo, negativo ou zero usando a estrutura if, elif e else.
'''

numero =  int(input("Digite o Numero: "))


if numero >= 1:
    print(f"O numero {numero} e Positivo")
elif numero  <= -1:
    print(f"Numero {numero} e Negativo")
else:
    print(f"Numero e {0}")