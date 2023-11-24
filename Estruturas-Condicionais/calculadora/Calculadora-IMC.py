###Calculadora de indice de massa corporal com tkinter ###
''' Utilizado a estruturas Condicionais if/elif/else para a declaração da saude'''


import tkinter as tk

def calcular_imc():
    altura = float(entry_altura.get())
    peso = float(entry_peso.get())
 
    imc = peso / altura**2
    
    label_resultado['text'] = "Seu IMC é: %.4f" % imc
 
    if imc < 16:
        label_classificacao['text'] = "Magreza grave"
    elif imc < 17:
        label_classificacao['text'] = "Magreza moderada"
    elif imc < 18.5:
        label_classificacao['text'] = "Magreza leve"
    elif imc < 25:
        label_classificacao['text'] = "Saudável"
    elif imc < 30:
        label_classificacao['text'] = "Sobrepeso"
    elif imc < 35:
        label_classificacao['text'] = "Obesidade Grau I"
    elif imc < 40:
        label_classificacao['text'] = "Obesidade Grau II (severa)"
    else:
        label_classificacao['text'] = "Obesidade Grau III (mórbida)"
 
root = tk.Tk()
root.title("Calculadora IMC")

menu_frame = tk.Frame()
menu_frame.pack()
 
frame_entrada = tk.Frame(root)
frame_entrada.pack()
 
label_altura = tk.Label(frame_entrada, text="Altura (m):")
label_altura.grid(row=0, column=0)
 
entry_altura = tk.Entry(frame_entrada)
entry_altura.grid(row=0, column=1)
 
label_peso = tk.Label(frame_entrada, text="Peso (Kg):")
label_peso.grid(row=1, column=0)
 
entry_peso = tk.Entry(frame_entrada)
entry_peso.grid(row=1, column=1)
 
frame_saida = tk.Frame(root)
frame_saida.pack()
 
label_resultado = tk.Label(frame_saida, text="")
label_resultado.pack()
 
label_classificacao = tk.Label(frame_saida, text="")
label_classificacao.pack()
 
botao_calcular = tk.Button(root, text="Calcular", command=calcular_imc)
botao_calcular.pack()

subtitle_label = tk.Label(root, text="by Danilo Silva", pady=10, padx=10 )
subtitle_label.pack()

root.mainloop()