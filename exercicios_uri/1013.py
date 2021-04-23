linha = input()
linha_splitada = linha.split(" ")

a, b, c = (map(int, linha.split(" ")))

resultado = (a+b+abs(a-b))/2
if (resultado > c):
    print("%d eh o maior" % (resultado))
else:
    print("%d eh o maior" % (c))
