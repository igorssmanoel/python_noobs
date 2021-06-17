from funcionario import Funcionario


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, carro):
        super().__init__(nome, cpf, salario)
        self.__carro = carro

    def __str__(self):
        return f"{self.get_bonificacao()} {self.get_salario()} {self.carro}"

    def get_bonificacao(self):
        return f"A bonificação é de R$ {(self.salario * 0.20):.2f}\n"

    def get_salario(self):
        return f"O salário é de R$ {self.salario:.2f}\n"

    @property
    def carro(self):
        return self.__carro

    @carro.setter
    def carro(self, value):
        self.__carro = value
