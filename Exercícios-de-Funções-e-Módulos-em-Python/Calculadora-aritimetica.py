import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

def clear():
    entry.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")

# Entrada
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0

for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, command=clear).grid(row=row, column=col)
    elif button == '=':
        tk.Button(root, text=button, command=evaluate).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, command=lambda key=button: press(key)).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Iniciar a interface gráfica
root.mainloop()
