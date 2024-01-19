class Veiculo:
    def __init__(self, marca:str, modelo:str, ano:int, cor:str):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, qtde_portas:int):
        super().__init__(marca, modelo, ano, cor)
        self.qtde_portas = qtde_portas

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas:int):
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas

carro1 = Carro(marca = "fiat", modelo = "uno", ano = 2004, cor = "Azul Escuro", qtde_portas= 2)
moto1 = Moto(marca = "honda", modelo = "XRE", ano = 2020, cor = "Preta", cilindradas = 300)

print(carro1.qtde_portas)
print(moto1.cilindradas)