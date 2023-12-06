# Exercício 3: Manipulação de Tuplas:

'''
Crie uma tupla com nomes de países. Escreva um programa que solicite ao usuário por um país e verifique se ele está na tupla.
Se estiver, imprima a posição (índice) do país na tupla.
'''

Paises = ("Estados Unidos",
"Canadá",
"Brasil",
"França",
"Japão",
"Austrália",
"Alemanha",
"Índia",
"China",
"Rússia",
"Itália",
"México",
"África do Sul",
"Argentina",
"Reino Unido")

nome = str(input("Digite o nome do pais: "))
nome_capitalizado = nome.capitalize() # Capitalizar a primeira letra do nome

index = Paises.index(nome_capitalizado) # Fornecer o index da lista

if nome_capitalizado in Paises:    
    print(f"O Pais {nome_capitalizado}, ser encontra no Index {index}")
else:
    print(f"{nome_capitalizado} não encontrado na lista de países.")