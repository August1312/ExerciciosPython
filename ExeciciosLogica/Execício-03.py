# Tipos de Dados (Tuplas):
'''
Crie uma tupla com nomes de frutas. 
Escreva um programa que pergunte ao usuário por uma fruta e verifique se ela está na tupla.
'''

frutas = {'morango', 'laranja', 'abacaxi', 'melão'}

verificar = str(input('Digite o nome da fruta: '))
verificar1 = str(input('Digite o nome da fruta: '))



if verificar in frutas and verificar1 in frutas:
    print(f'A lista contém tanto "{verificar}" quanto "{verificar1}"')
elif verificar in frutas:
      print(f'A lista contém apenas "{verificar}" e não "{verificar1}"')
elif verificar1 in frutas:
     print(f'A lista contém apenas "{verificar1}" e não "{verificar}"')
else:
     print(f'A lista não contém nem "{verificar}" nem "{verificar1}"')