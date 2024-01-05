from tkinter import *

caixinha = Tk()
caixinha.title("Aprendendo o place")
caixinha.geometry("300x300")

nome_label = Label(text="Digite seu nome:")
nome_label.place(x=15, y=10)
nome_input= Entry()
nome_input.place(x=110, y=12)

idade_label = Label(text="Digite sua idade:")
idade_label.place(x=15, y=40)
idade_input= Entry()
idade_input.place(x=110, y=40)


botao= Button(text="Enviar")
botao.place(x=130, y=70)





caixinha.mainloop()