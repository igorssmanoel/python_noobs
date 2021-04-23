numero_a = int(input("Digite um inteiro: "))  # Ler inteiro
numero_b = int(input("Digite outro inteiro: "))  # Ler outro Inteiro

# %s String
# %f Float
# %d Inteiro

print("Exemplo string: %s\nint: %d\nfloat: %.2f\n" % ("EXEMPLO DE STRING", 2, 3.5))

if (numero_a > numero_b):
    print("O numero %d eh maior que o numero %d" % (numero_a, numero_b))
elif (numero_a == numero_b):
    print("O numero %d eh igual ao numero %d" % (numero_a, numero_b))
else:
    print("O numero %d eh maior que o numero %d" % (numero_a, numero_b))

