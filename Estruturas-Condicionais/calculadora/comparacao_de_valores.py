### Comparação de valores com estruturas condicionais if/else ###
'''
Ele utiliza a estrutura condicional if para realizar a comparação e exibe o resultado na saída padrão. 
O script é uma ferramenta simples para demonstrar a lógica de controle de fluxo em Python ao comparar valores inseridos pelo usuário.
'''


primeiro_valor = input('digie um valor: ')
segundo_valor = input('digite um valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor= } é maior   '
        f' que {segundo_valor= }'
    )
else:
    print(
        f'{segundo_valor= } e maior que '
        f'que {primeiro_valor= }'
    )