import tkinter as tk
from tkinter import messagebox as msg

janela = None
contatos = []

def incluir():
  nome = entry_nome.get()
  celular = entry_celular.get()
  email = entry_email.get()

  if nome and celular and email:
    contato = f"{nome} - {celular} - {email}"
    contatos.append(contato)

    entry_nome.delete(0, tk.END)
    entry_celular.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    entry_nome.focus_set()

    dados_lista_box()
  else:
    msg.showwarning("Aviso", "Preencha todos campos.")
  
def dados_lista_box():
  lista_contatos.delete(0, tk.END)
  for item in contatos:
    lista_contatos.insert(tk.END, str(item))
  

def interface():
  global entry_nome, entry_celular, entry_email, lista_contatos

  quadro = tk.Frame(janela)
  quadro.pack(padx=20, pady=20, fill="both", expand=True)

  label_nome = tk.Label(quadro, text="Nome:")
  label_nome.pack(anchor='w')
  entry_nome = tk.Entry(quadro, width=50)
  entry_nome.pack()

  label_celular = tk.Label(quadro, text="Celular:")
  label_celular.pack(anchor='w')
  entry_celular = tk.Entry(quadro, width=50)
  entry_celular.pack()
  
  label_email = tk.Label(quadro, text="Email:")
  label_email.pack(anchor='w')
  entry_email = tk.Entry(quadro, width=50)
  entry_email.pack()

  frame_botoes = tk.Frame(quadro)
  frame_botoes.pack(pady=10)

  bt_incluir = tk.Button(frame_botoes, text="Incluir", command=incluir)
  bt_buscar = tk.Button(frame_botoes, text="Buscar")

  bt_incluir.grid(row=0, column=0, padx=10, pady=0)
  bt_buscar.grid(row=0, column=1, padx=0, pady=0)

  lista_contatos = tk.Listbox(quadro, width=50)
  lista_contatos.pack(padx=10, pady=10)
  
def main():
  global janela
  janela = tk.Tk()
  janela.title("Agenda de Contatos")
  interface()
  janela.mainloop()

main()
