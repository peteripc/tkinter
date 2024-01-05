from tkinter import *

janelinha = Tk()
janelinha.title("revisão")
janelinha.geometry("350x350")


def calcular_nota():
    NotaM = float(nota_matemática.get())
    NotaP = float(nota_português.get())
    NotaB = float(nota_biologia.get())
    média = (NotaM +  NotaP + NotaB)/3


    if média == 10:
        resposta.configure(text=f"Média {média}. Aprovado com distinçao", bg="blue")

    elif média > 10:
        resposta.configure(text=f"Notas inválidas")

    elif média >= 7 and média < 10:
        resposta.configure(text=f"Média {média}. Aprovado", bg="green")
    
    else:
        resposta.configure(text=f"Média {média}. Reprovado", bg="red")



aluno = Label (text= "digite o nome do aluno")
Aluno = Entry()
aluno.pack()
Aluno.pack()


matemática = Label (text= "digite a nota dele em matemática: ")
nota_matemática = Entry()
matemática.pack()
nota_matemática.pack()


português = Label (text= "digite a noda dele em portugês: ")
nota_português = Entry()
português.pack()
nota_português.pack()


biologia = Label (text="digite a nota dele em biologia: ")
nota_biologia = Entry()
biologia.pack()
nota_biologia.pack()



botão = Button(janelinha, text="enviar", command=calcular_nota)
botão.pack()



resposta = Label(text="Bem vindo")
resposta.pack()



janelinha.mainloop()