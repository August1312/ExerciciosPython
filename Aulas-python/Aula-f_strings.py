# Atribuir valores às variáveis
a = 'A'
b = 'B'
c = 1.1

# A ordem das chaves na string de formatação corresponde à ordem dos valores passados para o método .format()

# A primeira chave se refere ao primeiro valor da ordem no método .format()
string_formatada = 'a={nome1} b={nome2} c={nome3:.2f}'

# Usar o método .format() para substituir os marcadores de posição na string de formatação pelos valores correspondentes
resultado_formatado = string_formatada.format(nome1=a, nome2=b, nome3=c)

# Imprimir o resultado formatado
print(resultado_formatado)