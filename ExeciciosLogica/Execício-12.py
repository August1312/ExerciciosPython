# Exercício 2: Manipulação de Listas:

'''
Crie duas listas de números e escreva um programa que calcule e imprima a soma dos elementos nas posições correspondentes das duas listas.

'''

lista01 = [14,12,1,3,4,6,19]
lista02 = [1,2,3,4,5,6,7,]

selecionar_posição_01 = int(input("Digite a posição da lista: "))
selecionar_posição_02 = int(input("Digite a posição da lista: "))

soma = lista01[selecionar_posição_01] + lista02[selecionar_posição_02]

print(soma)
