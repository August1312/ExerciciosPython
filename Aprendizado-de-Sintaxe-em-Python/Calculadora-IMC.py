# Solicitar ao usuário a altura e peso
altura_p = float(input('Altura (separada por ponto .): '))
peso_p = float(input('Peso (em kg): '))

# Calcular o IMC
imc = peso_p / (altura_p ** 2)

# Imprimir o resultado do IMC
print('Seu IMC é:', imc)