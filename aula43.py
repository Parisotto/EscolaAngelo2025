import customtkinter as tk # pip install customtkinter
from tkinter import messagebox as msg
from tkinter import Listbox, Scrollbar

janela = None
contatos = []
indice_selecionado = None

def carga():
  global contatos
  contatos = arquivo('r')
  dados_lista_box()

def arquivo(op = 'r', contato = ''):
  arquivo = 'contatos.txt'
  try:
    with open(arquivo, op) as arq:
      if op == 'r':
        return arq.readlines()
      elif op == 'a':
        arq.write(contato)
      elif op =='w':
        arq.writelines(contato)
  except:
    return []

def selecionar_contato(event):
  global indice_selecionado
  try:
    indice_selecionado = lista_contatos.curselection()[0]
  except:
    print("Nada selecionado")

  if indice_selecionado is not None:
    contato = contatos[indice_selecionado].split(" - ")
    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, contato[0])
    entry_celular.delete(0, tk.END)
    entry_celular.insert(0, contato[1])
    entry_email.delete(0, tk.END)
    entry_email.insert(0, contato[2].strip())

def editar():
  global indice_selecionado
  if indice_selecionado is not None:
    nome = entry_nome.get()
    celular = entry_celular.get()
    email = entry_email.get()

    if nome and celular and email:
      contatos[indice_selecionado] = f"{nome} - {celular} - {email}\n"
      arquivo('w', contatos)
      dados_lista_box()

      entry_nome.delete(0, tk.END)
      entry_celular.delete(0, tk.END)
      entry_email.delete(0, tk.END)
      entry_nome.focus_set()

def excluir():
  global indice_selecionado
  if indice_selecionado is not None:
    del contatos[indice_selecionado]
    arquivo('w', contatos)
    dados_lista_box()
    indice_selecionado = None
    entry_nome.delete(0, tk.END)
    entry_celular.delete(0, tk.END)
    entry_email.delete(0, tk.END)
  else:
    print("Sem indice selecionado")

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
      lista_contatos.event_generate('<<ListboxSelect>>')
    else:
      msg.showinfo("Atenção", "Contato não encontrado")
  else:
    msg.showerror("ERRO!", "Digite um nome, celular ou email para fazer a busca")

def incluir():
  nome = entry_nome.get()
  celular = entry_celular.get()
  email = entry_email.get()

  if nome and celular and email:
    contato = f"{nome} - {celular} - {email}\n"
    contatos.append(contato)
    arquivo('a', contato)

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
  bt_editar = tk.CTkButton(frame_botoes, text="Editar", command=editar)
  bt_excluir = tk.CTkButton(frame_botoes, text="Excluir", command=excluir)

  bt_incluir.grid(row=0, column=0, padx=10, pady=0)
  bt_buscar.grid(row=0, column=1, padx=10, pady=10)
  bt_editar.grid(row=1, column=0, padx=10, pady=10)
  bt_excluir.grid(row=1, column=1, padx=10, pady=10)

  # ListaBox com Scroll
  lista_contatos_frame = tk.CTkFrame(quadro)
  lista_contatos_frame.pack(padx=10, pady=10, expand=False)

  scrollbar = Scrollbar(lista_contatos_frame)
  scrollbar.pack(side="right", fill="y")

  lista_contatos = Listbox(
      lista_contatos_frame, width=50, 
      font=("Verdana", 12), bd=0,
      yscrollcommand=scrollbar.set
    )
  lista_contatos.pack(side="left", fill="both")
  lista_contatos.bind('<<ListboxSelect>>', selecionar_contato)
  
  scrollbar.config(command=lista_contatos.yview)
  
def main():
  global janela
  janela = tk.CTk()
  janela.title("Agenda de Contatos")
  interface()
  carga()
  janela.mainloop()

main()
