"""
09. Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa
"""
print("-Digite 6 Números Inteiros Pares;\n")

loop = 0
lista = []

while loop < 6:
    loop += 1
    valor = int(input(f"Digite o {loop}º número: "))

    if valor % 2 == 0:
        lista.append(valor)

    else:
        print("O valor digitado é inválido!")
        lista = []
        break

if lista != []:
    lista.reverse()
    print(f"\nLista Completa Inversa: {lista}")

else:
    print()
