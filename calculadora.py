import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        opcao = operacao.get()
        
        if opcao == "Soma":
            resultado = num1 + num2
        elif opcao == "Subtração":
            resultado = num1 - num2
        elif opcao == "Multiplicação":
            resultado = num1 * num2
        elif opcao == "Divisão":
            if num2 == 0:
                messagebox.showerror("Erro", "Divisão por zero não é permitida")
                return
            resultado = num1 / num2
        else:
            messagebox.showerror("Erro", "Selecione uma operação válida")
            return
        
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos")

root = tk.Tk()
root.title("Calculadora Python")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Digite o primeiro número:").grid(row=0, column=0)
entry_num1 = tk.Entry(frame)
entry_num1.grid(row=0, column=1)

tk.Label(frame, text="Digite o segundo número:").grid(row=1, column=0)
entry_num2 = tk.Entry(frame)
entry_num2.grid(row=1, column=1)

operacao = tk.StringVar()
operacao.set("Soma")

opcoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
tk.OptionMenu(frame, operacao, *opcoes).grid(row=2, columnspan=2)

tk.Button(frame, text="Calcular", command=calcular).grid(row=3, columnspan=2)

label_resultado = tk.Label(frame, text="Resultado:")
label_resultado.grid(row=4, columnspan=2)

root.mainloop()
