import customtkinter as tk # pip install customtkinter
from tkinter import messagebox as msg
from tkinter import Listbox

janela = None
contatos = []

def buscar():
  nome = entry_nome.get().lower().strip()
  celular = entry_celular.get().strip()
  email = entry_email.get().lower().strip()

  lista_contatos.select_clear(0, tk.END)

  if nome or celular or email:
    for i in range(0, lista_contatos.size()):
      if nome and nome in lista_contatos.get(i).lower():
        indice = i
        break
      elif celular and celular in lista_contatos.get(i):
        indice = i
        break
      elif email and email in lista_contatos.get(i).lower():
        indice = i
        break
      else:
        indice = None

    if lista_contatos.size() > 0 and indice != None:
      lista_contatos.selection_set(indice)
      lista_contatos.activate(indice)
      lista_contatos.see(indice)
    else:
      msg.showinfo("Atenção", "Contato não encontrado")
  else:
    msg.showerror("ERRO!", "Digite um nome, celular ou email para fazer a busca")

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

  quadro = tk.CTkFrame(janela)
  quadro.pack(padx=20, pady=20, fill="both", expand=True)

  label_nome = tk.CTkLabel(quadro, text="Nome:")
  label_nome.pack(anchor='w', padx=20)
  entry_nome = tk.CTkEntry(quadro, width=350, font=("Verdana", 12))
  entry_nome.pack(padx=20)

  label_celular = tk.CTkLabel(quadro, text="Celular:")
  label_celular.pack(anchor='w', padx=20)
  entry_celular = tk.CTkEntry(quadro, width=350)
  entry_celular.pack()
  
  label_email = tk.CTkLabel(quadro, text="Email:")
  label_email.pack(anchor='w', padx=20)
  entry_email = tk.CTkEntry(quadro, width=350)
  entry_email.pack()

  frame_botoes = tk.CTkFrame(quadro)
  frame_botoes.pack(pady=10)

  bt_incluir = tk.CTkButton(frame_botoes, text="Incluir", command=incluir)
  bt_buscar = tk.CTkButton(frame_botoes, text="Buscar", command=buscar)
  bt_editar = tk.CTkButton(frame_botoes, text="Editar")
  bt_excluir = tk.CTkButton(frame_botoes, text="Excluir")

  bt_incluir.grid(row=0, column=0, padx=10, pady=0)
  bt_buscar.grid(row=0, column=1, padx=10, pady=10)
  bt_editar.grid(row=1, column=0, padx=10, pady=10)
  bt_excluir.grid(row=1, column=1, padx=10, pady=10)

  lista_contatos = Listbox(quadro, width=50, font=("Verdana", 12), bd=0)
  lista_contatos.pack(padx=10, pady=10)
  
def main():
  global janela
  janela = tk.CTk()
  janela.title("Agenda de Contatos")
  interface()
  janela.mainloop()

main()
