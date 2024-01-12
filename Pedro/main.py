class Carro:
    def __init__(self, marca:str, cor:str, modelo:str, ano:int, qtde_portas:int):
        self.marca = marca
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.qtde_portas = qtde_portas
    
carro1 = Carro(marca="ford", cor="preta", modelo="KA", ano=2019, qtde_portas=4)
carro2 = Carro



class Moto:
    def __init__(self, marca:str, modelo:int, cilindradas: int, cor:str):
        self.marca = marca
        self.modelo= modelo
        self.cilindradas = cilindradas
        self.cor = cor

    def buzinar(self):
        return f"o {self.modelo} está buzinando"
    
    def ligar(self):
        return f"a moto {self.modelo} ligou"
        
    def ver_informacoes(self):
        return f"""
        marca: {self.marca}
        modelo: {self.modelo}
        cilidradas: {self.cilindradas}
        cor: {self.cor}
        """
    

moto1 = Moto(marca="honda", modelo="titan", cilindradas=150, cor="preta")
moto2 = Moto(marca="honda", modelo="broz", cilindradas=170, cor="branca")
moto3 = Moto(marca="Yamaha", modelo="factor", cilindradas=200, cor="vermelha")


# print(f"{moto1.marca},\n{moto2.cilindradas, moto2.cor},\n{moto3.marca, moto3.cor, moto3.cilindradas, moto3.modelo}")

print(moto2.ver_informacoes())
