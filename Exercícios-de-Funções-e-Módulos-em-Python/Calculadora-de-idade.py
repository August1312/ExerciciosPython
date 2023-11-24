from datetime import datetime

#calcula a idade pelo datetime

def calcular_idade(data_nascimento):
    hoje = datetime.now()
    nascimento = datetime.strptime(data_nascimento, '%d-%m-%Y')
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day)< (nascimento.month, nascimento.day))
    return idade

#solicita a data de nascimento ao usuário

def main():
    data_nascimento = input("Digite a data de nascimento (formato DD-MM-YYYY): ")

#calcula a idade
    idade = calcular_idade(data_nascimento)

#ixibe a idade na tela 
    print("\n")
    print("-"*30)
    print(f"A Sua idade é: {idade} anos")
    print("\n")
    print("-"*30)

if __name__ == "__main__":
    main()
