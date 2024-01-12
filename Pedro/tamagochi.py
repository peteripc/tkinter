class Tamagotchi():
    def __init__(self, nome, especie, energia):
        self.nome = nome
        self.especie = especie
        self.energia = energia

    def brincar(self):
        if self.energia >=5:
            self.energia = self.energia - 5
        else:
            print("tu tá muito é com fome")
        return self.energia
    
    def comer(self):
        if self.energia <= 95:
            self.energia = self.energia + 5
        else:
            print("Tu tá de barriga cheia. vai brincar")
        return self.energia
    

tamagotchi1 = Tamagotchi(nome="bacurin", especie="aquática", energia = 100)


while True:
    menu = int(input("""
    escolha uma opção;
    1 - Brincar
    2 - Comer
    0 = Sair
"""))
    
    match menu: 
        case 1: 
            tamagotchi1.brincar()
        case 2:
            tamagotchi1.comer()
        case _:
            print("Opção inválida")
    
    print(f"energia atual: {tamagotchi1.energia}")
