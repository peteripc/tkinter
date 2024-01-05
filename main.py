from tkinter import  *
# Com essas variáveis você cria a janela, seu título e seu tamanho. A função serve para o botão
janelinha = Tk()
janelinha.title("revisão")
janelinha.geometry("350x350")

def saudacao():
    nome_digitado = nome_input.get()
    resposta.configure(text=f"seja bem vindo {nome_digitado}")

# com esses comandos você cria um nome na janela e altera c cor da barra e acor da fonte. com o comando de baixo você adiciona o nome na janela
nome_label = Label(text="digite seu nome: ", bg="red", fg="white")
nome_label.pack()

# Com esse comando você cria uma caixa de texto na janela. E com o pacl você a adiciona na janela
nome_input = Entry()
nome_input.pack()

# o comando botão funciona diferentemente. Você precisa adicionar ele na janela logo de início.
# o botão precisa da função para executar esta. 
botão = Button(janelinha, text="enviar", command=saudacao)
botão.pack()


#fazemos isso para que o texto digitado no botão apareça na própria janela. O "configure" na função serve para por o texto an janela
resposta = Label(text="Bem vindo")
resposta.pack()



janelinha .mainloop()