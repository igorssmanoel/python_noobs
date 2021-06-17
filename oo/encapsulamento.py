# self._atributo_encapsulado // Não pode ser alterado por fora, somente por métodos da classe

class Encap:
    def __init__(self):
        self.__attr_encapsulado = "Nao visivel"
        self.__valor_qualquer = 2

    """
        @description Getter
    """
    @property
    def attr_encapsulado(self):
        print("chamou o getter")
        return self.__attr_encapsulado + "teste2"

    @attr_encapsulado.setter
    def attr_encapsulado(self, value):
        if value > 3:
            print("Valor maior que 3")
        else:
            self.__attr_encapsulado = "teste3"


encap = Encap()

print(encap.attr_encapsulado)
encap.attr_encapsulado = 5
print(encap.attr_encapsulado)
