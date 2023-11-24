#Jogo simples automatizado em python no qual
#o computador escolhe aleatoriamente para ambos os jogadores


count_h =0
count_c =0
print("_____________________Pedra...Papel...Tesoura_____________\n")
print("Bem-vindo ao jogo. Vamos começar...\n")
keep_playing = True
while keep_playing:
    import random

    c_choice = random.choice(['Pedra', 'Papel', 'Tesoura'])
    print('o computador escolhe: ' + c_choice) 
    h_choice = random.choice(['Pedra', 'Papel', 'Tesoura'])
    print('Humano escolher: ' + h_choice)

    
    if((h_choice=='Pedra' and c_choice=='Tesoura') or (h_choice=='Tesoura' and c_choice=='Papel') or (h_choice=='Papel' and c_choice=='Pedra')):
        print("vitória humana")
        count_h += 1 

    elif(h_choice == c_choice):
        print('Empate')
        
    else :
        print("o computador vence")
        count_c += 1

        print("\nVocê quer jogar novamente?")
        answer = input()
        
        if answer == 'n':
            keep_playing = False
            print("\nObrigado por jogar")
            print("\nA pontuação do computador é: " + str(count_c))
            print("\nA pontuação do humana é: " + str(count_h))

            print("\nResultados gerais:")
        if count_c > count_h:
            print("Melhor sorte na próxima vez!\n")
        elif count_c == count_h:
            print("É um empate\n")
        else :
            print("Você venceu!\n")

        print("_____________________Pedra...Papel...Tesoura_____________\n")