"""
54. Faça um programa que receba um número inteiro maior doque 1, e verifique se o número fornecido
é primo ou não.
"""
nmr = int(input("-Digite um número inteiro:"))

mult = 0

for count in range(2, nmr):
    if (nmr % count == 0):
        print(f"-Multiplo de {count}.")
        mult += 1

if (mult == 0):
    print("\n-O Número é Primo!")
else:
    print("\n-O Número Não é Primo!")
