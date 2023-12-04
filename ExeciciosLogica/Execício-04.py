# Tipos de Dados (Dicionários):

'''Crie um dicionário com nomes e idades.
Escreva um programa que peça ao usuário por um nome e imprima a idade correspondente.
'''
# Lista de tuplas com nomes e números de telefone
contatos_lista = [('yan', '1234-5678'), ('pedro', '9999-9999'), ('ana', '8765-4321'), ('mariana', '8877-7788')]

# Converte a lista em Dicionário
contato = dict(contatos_lista)

procura = str(input('Nome do contato: '))

# Verifica se o nome está presente no dicionário e imprime o telefone correspondente
if procura in contato:
    print(f'O Telefone de {procura} é: {contato[procura]}')
else:
    print(f'Não existe esse {procura} na lista de contatos:')