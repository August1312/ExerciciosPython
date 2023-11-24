from faker import Faker
from faker.providers import credit_card 

#!Uso exclusivamente para fins de teste; não me responsabilizo por qualquer uso indevido por terceiros.

#Cria uma instância do Faker para dados em português do Brasil

fake = Faker('pt_BR')

#Lista para armazenar os conjuntos de dados

dados_fake = []

#Gera  5 conjutos de dados diferentes

for _ in range(5):
  nome_completo = fake.name()
  email = fake.email()
  endereco_completo = fake.address()
  telefone = fake.phone_number()
  empresa = fake.company()
  cpf = fake.cpf()
  numero_cartao = fake.credit_card_number()
  data_validade = fake.credit_card_expire()
  cvv = fake.credit_card_security_code()
  rg = fake.random_number(digits=9)
  separação = ("-"*30) 
  espaço = ("\n")

#Adiciona os dados gerados à lista

  dados_fake.append({
  "Nome": nome_completo,
  "Telefone": telefone,
  "Email": email,
  "Endereço": endereco_completo,
  "CPF": cpf,
  "RG": rg,
  "": espaço,
  "Dados cartão"
   :separação,
  "Numero Cartao de Credito": numero_cartao,
  "Validade": data_validade,
  "CVV": cvv })

#exibir os dados na tela 
for i, dados in enumerate(dados_fake, start=1):
    print("-"*30) 
    print(f"Dados Fake {i}:")
    for chave, valor in dados.items():
        print(f" {chave}: {valor}")
    print("-"*30) 