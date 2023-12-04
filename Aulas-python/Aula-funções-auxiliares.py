# Escreva funções auxiliares em vez de expressões complexas


from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)  # 'parse_qs e usado para decodificar a string de consulta.
'''
 keep_blank_values=True significa que os valores em branco também serão mantidos.
 Após a execução desta linha, a variável my_values conterá um dicionário onde as chaves
são os parâmetros da string de consulta e os valores são listas de valores associados a esses parâmetros.

'''
print('\n')
print(my_values)

# Impressão dos valores usando o método 'get':
'''
 Aqui, estamos usando o método get do dicionário resultante para obter os valores associados às 
chaves 'red', 'green' e 'opacity'. O método get retorna None se a chave não estiver presente,
o que é útil para evitar erros.

'''
print('\n')
print('Red: ',my_values.get('red'))
print('Green: ',my_values.get('green'))
print('Opacity: ',my_values.get('opacity'))

print('\n')


# Atribui o valor associado à chave 'red' ou 0 se a chave não estiver presente
red = my_values.get('red', [''])[0] or 0

# Atribui o valor associado à chave 'green' ou 0 se a chave não estiver presente
green = my_values.get('green', [''])[0] or 0

# Atribui o valor associado à chave 'opacity' ou 0 se a chave não estiver presente
opacity = my_values.get('opacity', [''])[0] or 0

print('\n')
print('Red: %r' % red)
print('Green: %r' % green)
print('Opacity %r' % opacity)
print('\n')
