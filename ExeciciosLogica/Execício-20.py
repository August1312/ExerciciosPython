# Exercício 10: Manipulação de Strings (Busca e Contagem):

'''
Crie uma string com uma frase que contenha algumas palavras repetidas.
Escreva um programa que solicite ao usuário por uma palavra e conte quantas vezes essa palavra aparece na frase.
'''


frase = "Python é uma linguagem de programação muito poderosa. Python é fácil de aprender. Com Python, você pode automatizar tarefas e desenvolver aplicativos."

consulta_palavra = str(input("Digite a Palavra para Consulta: "))

contagem = frase.lower().count(consulta_palavra.lower())

print(f"A palavra {consulta_palavra} aparece {contagem} de vezes.")