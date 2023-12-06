# Exercício 4: Manipulação de Dicionários:

'''
Crie um dicionário com produtos e seus preços.
Escreva um programa que solicite ao usuário 
por um produto e imprima o preço correspondente. 
Se o produto não estiver no dicionário, imprima uma mensagem indicando isso.
'''

LISTA_DE_PRODUTO = {
    "Iphone": 1500,
    "Samsung": 2500,
    "Xaiomi": 3500,
    "Motorola": 1200,
    "Lenovo": 3000
}

produto = str(input("Digite o Produto para Consulta: "))
produto_capializado = produto.capitalize()



if produto_capializado in LISTA_DE_PRODUTO:
    valor = LISTA_DE_PRODUTO[produto_capializado]
    print(f"O valor do {produto_capializado} e {valor}")

else:
     print(f"{produto_capializado} não encontrado na lista de produtos.")