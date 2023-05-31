"""
07. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
"""
print("-Descubra a média de 10 valores inteiros positivos.")
soma = 0
for n in range(1, 10 +1):
    num = int(input(f"Digite o {n}° valor:"))
    if num > 0:
        soma = soma + num
        media = soma / 10
print(f"A média dos valores é; {media}")
