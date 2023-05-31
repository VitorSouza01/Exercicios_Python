"""
02. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
"""

lp = 0
vlr_lst = []

while lp <= 5:
    vlr = int(input("Digite um valor inteiro: "))
    lp += 1
    vlr_lst.append(vlr)

print(f"\nOs valores digitados foram: {vlr_lst}")

