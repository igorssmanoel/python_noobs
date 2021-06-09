qtd = int(input())
for i in range(qtd):
    a, b = input().split()
    tam_b = len(b)

    if a[-tam_b:len(a)] == b:
        print("encaixa")
    else:
        print("nao encaixa")
