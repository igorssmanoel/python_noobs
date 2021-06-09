def fibonnacci(anterior, atual, qtd_max, lista_valores=[0, 1]):
    if len(lista_valores) >= qtd_max:
        return lista_valores
    aux = anterior
    anterior = atual
    atual += aux
    lista_valores.append(atual)
    return fibonnacci(anterior, atual, qtd_max, lista_valores)


def imprime_fibonnaci(lista):
    #print(" ".join(map(str,lista)))
    print(*lista)
    

qtd_max = int(input())
imprime_fibonnaci(fibonnacci(0, 1, qtd_max))
