# Manipulação de Strings (Concatenação e Comprimento):

'''
Peça ao usuário para digitar seu nome e sobrenome.
Em seguida, imprima a concatenação dos dois e o comprimento total.
'''

nome = str(input('\n Digite Seu Nome: '))
sobrenome = str(input('\n Digite Seu Sobrenome: '))


nome_completo = nome + ' ' + sobrenome

contagem_letra = 0

for caractere in nome_completo:
    if caractere.isalpha():
        contagem_letra += 1
    
    
print(f'Seu nome Completo é : {nome_completo} é tem {contagem_letra} Letras nele.')