from tkinter import *

janela = Tk()
janela.title("Aprendendo grid")
janela.geometry("400x400")


name_label= Label(text="digite seu nome")
name_label.grid(row=0, column=0)
name_input= Entry()
name_input.grid(row=0, column=1)


idade_label= Label(text="digite sua idade")
idade_label.grid(row=1, column=0)
idade_input= Entry()
idade_input.grid(row=1, column=1)


botao = Button(janela, text="Enviar", width=38)
botao.grid(row=2, column=0, columnspan=2)

janela.mainloop()