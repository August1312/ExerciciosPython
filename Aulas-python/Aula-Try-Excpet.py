# Introdução ao try/except
# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar

# Solicitar ao usuário para digitar um número
numero_str = input('Digite um número: ')

try:
    # Tentar converter a entrada para um número float
    numero_float = float(numero_str)
    
    # Se a conversão for bem-sucedida, imprimir o número e seu dobro
    print('Número Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except ValueError:
    # Se ocorrer um ValueError (por exemplo, se o usuário inserir algo que não é um número),
    # imprimir uma mensagem indicando que não é um número válido
    print('Erro: Isso não é um número válido')
