from funcionario import Funcionario
class Diretor(Funcionario):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def __str__(self):
        return f"{self.get_bonificacao()}"
    def get_bonificacao(self):
        return f"A bonificação é de R${(self.salario * 0.50):.2f}"

        
    