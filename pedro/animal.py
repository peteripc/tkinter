class Animal:
    def __init__(self, nome:str,raca:str, idade:int, cor:str):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.cor = cor
    
    def emitir_som(self):
        return "som indefinido"
    

class Gato(Animal):
    def __init__(self, nome: str, raca: str, idade: int, cor: str):
        super().__init__(nome, raca, idade, cor)

    def emitir_som(self):
        return "miau"

class Cachorro(Animal):
    def __init__(self, nome: str, raca: str, idade: int, cor: str):
        super().__init__(nome, raca, idade, cor)
    
    def emitir_som(self):
        return "au au"
    
gatin = Gato(nome = "xaninho", raca = "dos pretos", idade = 11, cor = "cinza")
dogin = Cachorro(nome = "nina", raca = "vira-lata", idade = 2, cor = "preto")
porco = Animal(nome = "pig", raca = "não definida", idade = 14, cor = "rosa")

print(gatin.emitir_som())
print(dogin.emitir_som())
print(porco.emitir_som())