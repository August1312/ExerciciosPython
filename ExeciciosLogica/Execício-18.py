# Exercício 8: Recursividade:

'''
Implemente uma função recursiva que calcule o fatorial de um número.
Em seguida, chame a função com um número e imprima o resultado.
'''

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


numero = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(numero)

print(f"O fatorial de {numero} é {resultado}")
