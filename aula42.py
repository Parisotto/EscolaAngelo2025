import tkinter as tk
from tkinter import messagebox as msg

janela = tarefa = listaBox = None

def adicionar():
  novaTarefa = tarefa.get()
  if novaTarefa:
    listaBox.insert(tk.END, novaTarefa)
    tarefa.delete(0, tk.END)
  else:
    msg.showwarning("Aviso", "Digite uma tarefa")

def interface():
  global tarefa, listaBox

  rotulo = tk.Label(janela, text="Tarefa")
  rotulo.pack(pady=10)

  tarefa = tk.Entry(janela, width=70)
  tarefa.pack(pady=(0, 10), padx=20)

  bt_adicionar = tk.Button(janela, text='Adicionar Tarefa', command=adicionar)
  bt_adicionar.pack(pady=10)

  listaBox = tk.Listbox(janela, width=70, height=10)
  listaBox.pack(padx=20, pady=10)

  bt_concluir = tk.Button(janela, text="Cocluir")
  bt_concluir.pack(pady=10)


def main():
  janela = tk.Tk()
  janela.title("Gerenciador de Tarefas")
  interface()
  janela.mainloop()

main()