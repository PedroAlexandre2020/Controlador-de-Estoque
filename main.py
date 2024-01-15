from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from view import *
from tkinter import messagebox

cor0 = "#f0f3f5"
cor1 = "#feffff"
cor2 = "#4fa882"
cor3 = "#38576b"
cor4 = "#403d3d"
cor5 = "#e06636"
cor6 = "#038cfc"
cor7 = "#ef5350"
cor8 = "#263238"
cor9 = "#e9edf5"

janela = Tk()
janela.title("Teste")
janela.geometry('1043x453')
janela.configure(background=cor0)
janela.resizable(width=FALSE, height=FALSE)

frame_cima = Frame(janela, width=310, height=50, bg=cor2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=cor1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=cor1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

### Label da parte superior ###
app_nome = Label(frame_cima, text='Cadastro de Produtos', anchor=NW, font=('Ivy 13 bold'), bg=cor2, fg=cor1, relief='flat')
app_nome.place(x=10, y=20)

global tree

def inserir():
    nome = e_nome.get()
    fornecedor = e_fornecedor.get()
    date = e_date.get()
    preco = e_preco.get()
    estoque = e_estoque.get()
    observacao = e_obs.get()

    lista = [nome, fornecedor, date, preco, estoque, observacao]

    if nome=='':
        messagebox.showerror('Erro', 'O nome nao pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showerror('Sucesso', 'Os dados foram inseridos com sucesso')

        e_nome.delete(0, 'end')
        e_fornecedor.delete(0, 'end')
        e_date.delete(0, 'end')
        e_preco.delete(0, 'end')
        e_estoque.delete(0, 'end')
        e_obs.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()



def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0, 'end')
        e_fornecedor.delete(0, 'end')
        e_date.delete(0, 'end')
        e_preco.delete(0, 'end')
        e_estoque.delete(0, 'end')
        e_obs.delete(0, 'end')

        e_nome.insert(0, tree_lista[1])
        e_fornecedor.insert(0, tree_lista[2])
        e_date.insert(0, tree_lista[3])
        e_preco.insert(0, tree_lista[4])
        e_estoque.insert(0, tree_lista[5])
        e_obs.insert(0, tree_lista[6])
        
        def update():
            nome = e_nome.get()
            fornecedor = e_fornecedor.get()
            date = e_date.get()
            preco = e_preco.get()
            estoque = e_estoque.get()
            observacao = e_obs.get()

            lista = [nome, fornecedor, date, preco, estoque, observacao, valor_id]

            if nome=='':
                messagebox.showerror('Erro', 'O nome nao pode ser vazio')
            else:
                atualizar_info(lista)
                messagebox.showerror('Sucesso', 'Os dados foram atualizados com sucesso')

                e_nome.delete(0, 'end')
                e_fornecedor.delete(0, 'end')
                e_date.delete(0, 'end')
                e_preco.delete(0, 'end')
                e_estoque.delete(0, 'end')
                e_obs.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()


        # Botão de atualizar

        b_confirmar = Button(frame_baixo, command=update , text='Confirmar', width=10, font=('Ivy 7 bold'), bg = cor2, fg = cor1, relief = 'raised')
        b_confirmar.place(x=110, y = 380)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela')


def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]
        deletar_info(valor_id)
        messagebox.showinfo('Sucesso', 'Os dados foram deletados da tabela com sucesso')

        for widget in frame_direita.winfo_children():
                widget.destroy()
        
        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')


### Frame da parte inferior ###

# Nome
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y = 40)

# Fornecedor
l_fornecedor = Label(frame_baixo, text='Fornecedor *', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
l_fornecedor.place(x=10, y= 70)
e_fornecedor = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_fornecedor.place(x=15, y = 100)

# Data de Consulta
l_date = Label(frame_baixo, text='Data de Entrega *', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
l_date.place(x=10, y= 130)
e_date = DateEntry(frame_baixo, width=40, background='darkblue', foreground='white', borderwidth=2)
e_date.place(x=15, y = 170)

# Preço
l_preco = Label(frame_baixo, text='Preço *', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
l_preco.place(x=10, y=200)
e_preco = Entry(frame_baixo, width=15, justify='left', relief='solid')
e_preco.place(x=15, y=230)

# Estoque
l_estoque = Label(frame_baixo, text='Estoque *', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
l_estoque.place(x=200, y=200)
e_estoque = Entry(frame_baixo, width=15, justify='left', relief='solid')
e_estoque.place(x=205, y=230)

# Observação
l_obs = Label(frame_baixo, text='Observação *', anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
l_obs.place(x=10, y=280)
e_obs = Entry(frame_baixo, width=40, justify='left', relief='solid')  # Ajuste o valor de height conforme necessário
e_obs.place(x=15, y=320)


# Botão de inserção

b_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=10, font=('Ivy 9 bold'), bg = cor6, fg = cor1, relief = 'raised')
b_inserir.place(x=15, y = 360)

# Botão de atualizar

b_editar = Button(frame_baixo, command=atualizar,  text='Editar', width=10, font=('Ivy 9 bold'), bg = cor2, fg = cor1, relief = 'raised')
b_editar.place(x=105, y = 360)

# Botão de deletar

b_deletar = Button(frame_baixo,command = deletar, text='Deletar', width=10, font=('Ivy 9 bold'), bg = cor7, fg = cor1, relief = 'raised')
b_deletar.place(x=190, y = 360)


### frame three ###
###### codigo para tabela ---------------

def mostrar():

    global tree

    lista = mostrar_info()

    ###lista para cabecario
    tabela_head = ['ID','Nome', 'Fornecedor', 'Data', 'Preço Unidade' , 'Estoque', 'Observações']


    ## criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    ### vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    ### horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        ###adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)



mostrar()
janela.mainloop()
