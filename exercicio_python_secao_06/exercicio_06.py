"""
06. Faça um programa que leia 10 inteiros e imprima sua média.
"""
print("-Digite 10 valores inteiros e descubra a média.")
soma = 0
for n in range(1, 10 +1):
    num = int(input(f"Digite o {n}° valor:"))
    soma = soma + num
    media = soma / 10
print(f"A média dos valores é; {media}")
