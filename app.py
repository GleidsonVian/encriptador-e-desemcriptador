from tkinter import * 
from tkinter import messagebox
import base64
import os

# Função para desencriptar a mensagem
def desemcriptar():
    senha = code.get()  # Obtém a senha inserida pelo usuário

    if senha == '1234':  # Verifica se a senha está correta
        # Cria uma nova janela para mostrar o texto desencriptado
        tela2 = Toplevel(tela)
        tela2.title('desemcriptado')
        tela2.geometry('400x200')
        tela2.configure(bg='#00bd56')

        # Obtém a mensagem do campo de texto
        mensagem = texto1.get(1.0, END)
        decode_mensagem = mensagem.encode('ascii')
        base64_bytes = base64.b64decode(decode_mensagem)  # Desencripta a mensagem
        encriptado = base64_bytes.decode('ascii')

        # Exibe o texto desencriptado na nova janela
        Label(tela2, text='DESENCRIPTADO', font='arial', fg='white', bg='#00bd56').place(x=10, y=0)
        texto2 = Text(tela2, font='RPbote 10', bg='white', relief='groove', wrap='word', bd=0)
        texto2.place(x=10, y=40, width=380, height=150)
        texto2.insert(END, encriptado)
    
    elif senha == '':  # Caso a senha não tenha sido inserida
        messagebox.showerror('encriptação', 'Insira uma senha')
    elif senha != '1234':  # Caso a senha esteja incorreta
        messagebox.showerror('encriptação', 'Senha Inválida')

# Função para encriptar a mensagem
def encriptar():
    senha = code.get()  # Obtém a senha inserida pelo usuário

    if senha == '1234':  # Verifica se a senha está correta
        # Cria uma nova janela para mostrar o texto encriptado
        tela1 = Toplevel(tela)
        tela1.title('encriptado')
        tela1.geometry('400x200')
        tela1.configure(bg='#ed3833')

        # Obtém a mensagem do campo de texto
        mensagem = texto1.get(1.0, END)
        encode_mensagem = mensagem.encode('ascii')
        base64_bytes = base64.b64encode(encode_mensagem)  # Encripta a mensagem
        encriptado = base64_bytes.decode('ascii')

        # Exibe o texto encriptado na nova janela
        Label(tela1, text='ENCRIPTADO', font='arial', fg='white', bg='#ed3833').place(x=10, y=0)
        texto2 = Text(tela1, font='RPbote 10', bg='white', relief='groove', wrap='word', bd=0)
        texto2.place(x=10, y=40, width=380, height=150)
        texto2.insert(END, encriptado)
    
    elif senha == '':  # Caso a senha não tenha sido inserida
        messagebox.showerror('encriptação', 'Insira uma senha')
    elif senha != '1234':  # Caso a senha esteja incorreta
        messagebox.showerror('encriptação', 'Senha Inválida')

# Função para criar a tela principal
def tela_principal():
    global tela
    global code
    global texto1

    # Função para resetar os campos de entrada
    def reset():
        code.set('')
        texto1.delete(1.0, END)

    tela = Tk()
    tela.geometry('375x398')

    # Ícone da janela
    imagem_icone = PhotoImage(file='chaves.png')
    tela.iconphoto(False, imagem_icone)

    tela.title('PctApp')

    # Label e campo de texto para inserção da mensagem
    Label(text='Insira seu texto para encriptação e desemcriptação', fg='black', font=('calibri', 13)).place(x=10, y=10)
    texto1 = Text(font='Robote 20', bg='white', relief='groove', wrap='word', bd=0)
    texto1.place(x=10, y=50, width=355, height=100)

    # Label e campo de entrada para a senha
    Label(text='Coloque sua senha para encriptar ou desemcriptar', fg='black', font=('calibri', 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=('arial', 25), show='*').place(x=10, y=200)

    # Botões para encriptar, desencriptar e resetar
    Button(text='ENCRIPTAR', height='2', width=23, bg='#ed3833', fg='white', bd=0, command=encriptar).place(x=10, y=250)
    Button(text='DESEMCRIPTAR', height='2', width=23, bg='#00bd56', fg='white', bd=0, command=desemcriptar).place(x=200, y=250)
    Button(text='RESET', height='2', width=50, bg='#1089ff', fg='white', bd=0, command=reset).place(x=10, y=300)

    tela.mainloop()

# Chama a função para iniciar a interface gráfica
tela_principal()
