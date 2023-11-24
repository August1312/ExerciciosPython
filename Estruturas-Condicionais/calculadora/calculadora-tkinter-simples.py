### Criando uma calculadora simples com tkinter para estudos de estruturas condicionais no Python. ###
'''
### Foi utilizado utilizado o basico do tkinter para esse execicio em python, sem muita complexidade. ###
### Foi utlizidado a cadeia de estrutura condicionais com  if/elif  no execicios. ####
### Foi Criada uma Class com nome Calculadora e Funçoes com {def} para  inicio da label do tkinter e para Calcula. ###
'''


from tkinter import ttk
import tkinter as tk

class Calculadora:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root

        # Cria as variáveis que armazenarão os operandos e o resultado
        self.operando1 = 0
        self.operando2 = 0
        self.resultado = 0

        # Cria os widgets da calculadora
        self.label_operando1 = tk.Label(self.root, text="Operando 1:")
        self.entry_operando1 = tk.Entry(self.root)
        self.label_operando2 = tk.Label(self.root, text="Operando 2:")
        self.entry_operando2 = tk.Entry(self.root)
        self.label_operador = tk.Label(self.root, text="Operador:")
        self.combo_operador = tk.ttk.Combobox(self.root, values=["+", "-", "*", "/"])
        self.button_calcular = tk.Button(self.root, text="Calcular", command=self.calcular)
        self.label_resultado = tk.Label(self.root, text="Resultado:")
        self.entry_resultado = tk.Entry(self.root)

        # Organiza os widgets na tela
        self.label_operando1.grid(row=0, column=0)
        self.entry_operando1.grid(row=0, column=1)
        self.label_operando2.grid(row=1, column=0)
        self.entry_operando2.grid(row=1, column=1)
        self.label_operador.grid(row=2, column=0)
        self.combo_operador.grid(row=2, column=1)
        self.button_calcular.grid(row=3, column=0)
        self.label_resultado.grid(row=4, column=0)
        self.entry_resultado.grid(row=4, column=1)

    def calcular(self):
        # Obtém os valores dos operandos
        self.operando1 = float(self.entry_operando1.get())
        self.operando2 = float(self.entry_operando2.get())

        # Calcula o resultado
        if self.combo_operador.get() == "+":
            self.resultado = self.operando1 + self.operando2
        elif self.combo_operador.get() == "-":
            self.resultado = self.operando1 - self.operando2
        elif self.combo_operador.get() == "*":
            self.resultado = self.operando1 * self.operando2
        elif self.combo_operador.get() == "/":
            self.resultado = self.operando1 / self.operando2

        # Atualiza o label do resultado
        self.entry_resultado.delete(0, tk.END)
        self.entry_resultado.insert(0, str(self.resultado))


root = tk.Tk()
Calculadora(root)
root.mainloop()
