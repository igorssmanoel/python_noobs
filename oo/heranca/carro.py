class Carro:
    def __init__(self, nome, marca, cor, ano):
        self.__nome = nome
        self.__marca = marca
        self.__cor = cor
        self.__ano = ano

    def __str__(self):
        return f"O Carro é o(a) {self.marca} {self.nome} cor {self.cor} ano {self.ano}"

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, value):
        self.__marca = value

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, value):
        self.__cor = value

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, value):
        self.__ano = value
