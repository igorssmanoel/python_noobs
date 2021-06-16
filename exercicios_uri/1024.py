# Na primeira passada,
# somente caracteres que sejam
# letras minúsculas e maiúsculas devem ser
# deslocadas 3 posições para a direita

# ord("A") => 65 converte em decimal da tabela ascii correspondente
# chr(65) converte em char da tabela ascii correspondente


def desloca(texto, deslocamento):
    texto_deslocado = ""
    for letra in texto:
        if letra.isalpha():
            texto_deslocado += chr(ord(letra) + deslocamento)
        else:
            texto_deslocado += letra

    return texto_deslocado


# Na segunda passada, a linha deverá ser invertida
def inverte(texto):
    return texto[::-1]

# Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII


def desloca_qualquer(texto, deslocamento):
    tamanho = len(texto)
    metade = tamanho // 2

    texto_deslocado = texto[0:metade]
    for index in range(metade, tamanho):
        texto_deslocado += chr(ord(texto[index]) + deslocamento)

    return texto_deslocado


qtd = int(input())

for i in range(qtd):
    valor = input()
    valor_deslocado = desloca(valor, 3)

    valor_invertido = inverte(valor_deslocado)

    resultado = desloca_qualquer(valor_invertido, -1)
    print(resultado)
