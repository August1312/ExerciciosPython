# converção de linha em tuplas e formatação de numeros 

nome = 'danilo silva dos santos'

altura = (1.80)

peso = (86)

imc = (peso / altura**2)

# conversão de todo comando de print para uma unica linha para melhor organiza o codigo.
#a converção de quantas casa vai ser mostrada pelo numero segue de ( .mais o numero de casas (2)seguido de F).
# F - strings 
linha_1 = f'{nome} tem {altura: .2f} de altura' 

linha_2 = f'{nome} voce pesa {peso} e seu imc é {imc: .2f}'

print(linha_1)

print(linha_2)

print('fim')