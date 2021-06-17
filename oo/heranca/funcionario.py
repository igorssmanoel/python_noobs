class Funcionario:
    def __init__(self, nome, cpf, salario, vt=4.50):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
        self.__vt = vt

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
        return self.__salario * 0.10

    @property
    def vt(self):
        return self.__vt

    @vt.setter
    def vt(self, value):
        self.__vt = value
