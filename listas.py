""" linha = input().split() """
linha = ['a', 'b', 3]
#         0    1   2
# acessar primeira posicao
print(linha[0])

# ultima posicao
print(linha[-1])
print(linha[len(linha)-1])

# penultima posicao
print(linha[-2])

texto = "igor manoel"

# posicao especifica
print(texto[0:4])

# ordenar lista
linha = [5, 3, 2, 9, 8]

linha.sort()                # Ordena em ordem crescente
print(linha)

linha.sort(reverse=True)    # Ordena em ordem decrescente
print(linha)

linha.append(12)            # Adiciona valor na lista
linha.append(12)
print(linha)

linha.pop()         # remove o ultimo item ou index passado por parametro

linha.remove(12)    # remove o primeiro item encontrado pelo valor
print(linha)


# Dicionario

dic = {"chave_1": 1, "chave_2": 2}

dic["chave_3"] = 3  # adicionar


dic.pop("chave_1")      # Remove item pela chave
del dic["chave_1"]      # Remove item pela chave

print(dic)
