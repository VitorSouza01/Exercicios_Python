"""
08. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""
print("-Descubra qual é o maior e o menor dos 10 valores!")
num = float(input('Digite o 1° numero: '))

nmr_menor = num
nmr_maior = num

for n in range(2, 11):
    num = float(input(f"Digite o {n}° valor: "))

    if num > nmr_maior:
         nmr_maior = num

    elif num < nmr_menor:
        nmr_menor = num

print(f"O valor maior é {nmr_maior}, e o valor menor é {nmr_menor}.")
