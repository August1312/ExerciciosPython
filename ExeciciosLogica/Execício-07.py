# Funções:

'''
Crie uma função que aceite dois parâmetros e retorne a soma deles. Em seguida,
chame a função com alguns valores e imprima o resultado.
'''

def Soma_de_dois_numeros(A, B):
    soma = A + B
    return soma

def Dividi_dois_numeros(A, B):
    dividi = A / B
    return dividi

def Multiplica_dois_numeros(A, B):
    mutiplica = A * B 
    return mutiplica

escolha_oque_fazer = str(input('Digite 1 (Soma), 2 (Dividi), 3 (Multiplica):'))

A = int(input('Digite numero A: '))
B = int(input('Digite numero B: '))

if escolha_oque_fazer in ['1', '2', '3']:
   if escolha_oque_fazer == '1':
    print(f'A Soma de {A} + {B} é: {Soma_de_dois_numeros(A, B)}')
   elif escolha_oque_fazer == '2':
    print(f'A Divisão de {A} / {B} é: {Dividi_dois_numeros(A, B)}')
   elif escolha_oque_fazer == '3':
    print(f'A Multiplicação de {A} * {B} é: {Multiplica_dois_numeros(A, B)}')
else:
    print(f'Por Favor escolha uma opção valida de 1 para somar, 2 para dividi, 3 para multiplicar')
