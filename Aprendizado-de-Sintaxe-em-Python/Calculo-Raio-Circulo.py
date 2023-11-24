### programa que pede o raio de um círculo, e em seguida exiba o perímetro e área do círculo ###
import math

raio = float(input("Digite o Raio do Circulo: "))


#Função para Calcula o circuferencia 
def Area_circuferencia_com_raio():
    circuferencia = math.pi * (raio**2)
    return circuferencia


def Perimetro_circuferencia():
    perimetro = 2 * math.pi * raio
    return perimetro


Area = Area_circuferencia_com_raio()
Perimetro = Perimetro_circuferencia()

print (f' Area do Círculo e {Area:.2f}')
print (f' Perimetro do Círculo e {Perimetro:.2f}')