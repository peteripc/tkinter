
from tkinter import *

janela = Tk()
janela.title("mercearia")
janela.geometry = ("700x700")

label = Label(janela, text="O que você deseja fazer? ")
label.pack()

botao1 = Button(janela, text= "cadastrar produtos.") 
botao1.pack()

botao2 = Button(janela, text= "Calcular lucro.")
botao2.pack()

botao3 = Button(janela, text="venda de alimentos")
botao3.pack()

janela.mainloop()
