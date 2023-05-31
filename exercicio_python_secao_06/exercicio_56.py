"""
56. Faça um programa que calcule a soma de todos os números primos abaixo de dois milhões.
"""

# CUIDADO AO RODAR O CÓDIGO! CÓDIGO MUITO PESADO!

print("-Descubra a soma de todos os números primos abaixo de dois milhões.")

n = 2000000

soma = 0
conta = 0
num = 2

while conta < n:

    cdg = True
    for i in range(2, num):
        if num % i == 0:
           cdg = False
           break

    if cdg:
        soma += num
        conta += 1
    num += 1

print(f"\n-A soma de todos os números primos até {n} é; {soma}.")
