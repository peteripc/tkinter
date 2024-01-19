class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Refrigerante(Produto):
    def __init__(self, marca, sabor, preco, quantidade):
        
        self.marca = marca
        self.sabor = sabor
        self.preco = preco
        self.quantidade = quantidade

class Biscoito(Produto):
    def __init__(self, marca, sabor, preco, tamanho):
        
        self.marca = marca
        self.sabor = sabor
        self.preco = preco
        self.quantidade = tamanho