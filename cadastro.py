"""
1) Importar as minhas bibliotecas
2) Criar interface gráfica:
    - Descrição
    - Tipo da Unidade
    - Qunatidade do tipo da Unidade
3) Inteligencia da Interface Gráfica:
    - Função
"""

import tkinter as  tk
import datetime as dt
from tkinter import ttk

Lista_tipos = ["Galão", "Caixa", "Saco", "Unidade"]
Lista_codigos = []

janela =  tk.Tk()

# Criação da Função

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quant.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(Lista_codigos) + 1
    codigo_str = "COD - {}".format(codigo)
    Lista_codigos.append((codigo_str, descricao, tipo, quant, data_criacao))

# Título da Janela
janela.title('Ferramenta de Cadastro de Materiais')

# Labels

label_descricao = tk.Label(text='Descrição do material')
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text='Tipo da Unidade do Material')
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=Lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quant = tk.Label(text='Qunatidade na Unidade de Material')
label_quant.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2 , padx=10, pady=10, sticky='nswe', columnspan=2)

botao_criar_codigo = tk.Button(text='Criar código', command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)


janela.mainloop()

print(Lista_codigos)