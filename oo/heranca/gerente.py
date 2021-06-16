from ..heranca import Funcionario


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def get_bonificacao(self):
        return self._salario * 0.20
