class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, value):
        self.__salario = value

    def get_bonificacao(self):
        return self._salario * 0.10
