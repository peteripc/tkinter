class Gato:
    def __init__(self, nome, raça, peso:float, idade:int, castrado:bool):
        self.nome = nome
        self.raça = raça
        self.peso = peso
        self.idade = idade
        self.castrado = castrado
    

    def miar(self, nome):
        print(f"O {nome} está miando. D~e atenção a ele!")

gato1 = Gato(nome ="tom",raça = "russo azul", peso = 2.45, idade = 4, castrado = True)
gato2 = Gato(nome ="meaoth",raça = "persa", peso = 4.2, idade = 7, castrado = False)

gato1.miar(gato1.nome)
    