class Fibonnacci():
    qtd_max = 0
    lista_valores = []

    def __init__(self, qtd_max):
        self.qtd_max = qtd_max
        self.lista_valores = [0, 1]

    def imprime_qtd_max(self):
        print(self.qtd_max)

    def calcula_fibonnacci(self, anterior=0, atual=1):
        if len(self.lista_valores) >= self.qtd_max:
            return self.lista_valores
        aux = anterior
        anterior = atual
        atual += aux
        self.lista_valores.append(atual)
        return self.calcula_fibonnacci(anterior, atual)

    def imprime_fibonnaci(self):
        print(*self.lista_valores)

