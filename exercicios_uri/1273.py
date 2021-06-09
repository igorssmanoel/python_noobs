qtd = int(input())
while qtd != 0:
    nomes = []
    maior = 0
    for i in range(qtd):
        nome = input()
        tam_nome = len(nome)
        if (tam_nome > maior):
            maior = tam_nome
        nomes.append(nome)

    for nome in nomes:
        print("%s%s" % (((maior-len(nome))*" "), nome))

    qtd = int(input())
    if qtd != 0:
        print()
