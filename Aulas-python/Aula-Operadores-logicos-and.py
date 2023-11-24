# Operadores lógicos
# and (e), or (ou), not (não)
# and - todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# são considerados falsy (que você já viu): 0, 0.0, '', False
# Também existe o tipo None que é usado para representar um não valor.
#
# not é usado para inverter valores booleanos: True vira False e False vira True
#
# Avaliação de curto-circuito

# entrada = input('[E]ntrar [S]air: ')
# senha = input('Senha: ')

# senha_permitida = '123456'

# if (entrada.lower() == 'e') and (senha == senha_permitida):
#     print('Entrar')
# else:
#     print('Sair')

# if not senha:
#     print('Digite a senha.')

# Operadores (in) e (not in)
# Strings são iteráveis

nome = input('Digite seu nome: ')
encontrar = input('O que você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
