# Exercício 7: Funções com Retorno Condicional:

'''
Crie uma função que aceite três parâmetros e retorne o maior deles.
Em seguida, chame a função com alguns valores e imprima o resultado.

'''

def maior_entre_numeros(a, b, c):
    return max(a, b, c)

a = int(input("Digite numero A: "))
b = int(input("Digite numero b: "))
c = int(input("Digite numero C: "))


resultado = maior_entre_numeros(a, b, c)

print(f"O maior numero é ({resultado})")