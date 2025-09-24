import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Cores personalizadas
COR_FUNDO = "#FFC0CB"  # Rosa claro
COR_BOTAO = "#FFFFFF"  # Branco
COR_TEXTO = "#FF1493"  # Rosa escuro

# Criando a janela com tamanho maior
janela = ttk.Window(themename="flatly")  
janela.title("Calculadora")
janela.geometry("400x550")  # Defini um tamanho maior
janela.configure(bg=COR_FUNDO)

# Criando o campo de entrada maior
entrada = ttk.Entry(janela, width=20, font=("Consolas", 30), bootstyle="light")
entrada.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

# Função para calcular
def clicar(botao):
    if botao == "=":
        try:
            resultado = eval(entrada.get())
            entrada.delete(0, ttk.END)
            entrada.insert(ttk.END, str(resultado))
        except:
            entrada.delete(0, ttk.END)
            entrada.insert(ttk.END, "Erro")
    elif botao == "C":
        entrada.delete(0, ttk.END)
    else:
        entrada.insert(ttk.END, botao)

# Criando botões maiores e arredondados
botoes = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for i, linha in enumerate(botoes):
    for j, botao in enumerate(linha):
        btn = ttk.Button(janela, text=botao, width=8, padding=15, bootstyle="secondary",
                         (command=lambda b=botao: clicar(b))
        btn.grid(row=i+1, column=j, padx=10, pady=10, ipadx=10, ipady=10)  # Botões maiores

# Rodando a interface
janela.mainloop()
