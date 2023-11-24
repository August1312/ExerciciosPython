### Analise de Nome com Estruturas Condicionais ###

''' verifica se o nome contém espaços, imprime o nome invertido, informa se o nome tem espaços ou não,
 e fornece detalhes adicionais sobre o comprimento e as extremidades do nome '''

nome = input('Digiti seu Nome: ')
idade = input('Digite sua Idade')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')

    else:
        print('Seu nome NÂO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print("Desculpe, voçê deixou campos vazios.")