from re import split, replace
words = []

output = []
while True:
    try:
        entrada = input()
        ci = split('[-+#.)( *$%:]', entrada.lower())
        output += ci
    except EOFError:
        break
output.sort()
output = list(filter(None, output))
output = [replace() for n in output if x.isalpha()]
