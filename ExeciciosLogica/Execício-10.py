# Manipulação de Strings (Métodos):

'''
Crie uma string com uma frase. 
Utilize os métodos de string para imprimir a frase em maiúsculas,
em minúsculas, substituir uma palavra e dividir a frase em palavras.
'''

frase = "Python é uma linguagem de programação poderosa e versátil."


# Frase em maiúsculas
print('\nFrase em Maiúscula: ',frase.upper())

# Frase em minusculas 
print('\nFrase em Minusculas: ',frase.lower())

palavra_substuitida = 'Python'
nova_palavra = 'Java'

frase_substituida = frase.replace(palavra_substuitida, nova_palavra)

print('\nNova Frase com Substituição: ', frase_substituida)


# Dividir a frase em palavras
palavras = frase.split()
print('\nPalavras na Frase: ', palavras)
