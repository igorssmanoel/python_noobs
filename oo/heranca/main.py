from gerente import Gerente
from carro import Carro


car = Carro("Fusca", "volkswagen", "azul", 1968)

gerente = Gerente("igor", "09443298961", 2000.00, car)

""" print(gerente.get_bonificacao())
print(gerente.get_salario()) """

print(gerente)
