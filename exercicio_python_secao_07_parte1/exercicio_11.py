"""
11. Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números
negativos e a soma dos números positivos desse vetor.
"""
import random

lst = []
lst_ngt = []
lst_pst = []

lp_ngt = 0
lp_pst = 0

for i in range(0,10):
    n = random.randint(-99, 99)
    lst.append(n)

    if n < 0:
        lst_ngt.append(n)
        lp_ngt += 1

    elif n > 1:
        lst_pst.append(n)
        lp_pst += n

print("Vetor com 10 números aleatorios;")
print(lst)
print(f"\nQuantidade de números nehativos: {lp_ngt}")
print(lst_ngt)
print(f"\nSoma dos números positivos: {lp_pst}")
print(lst_pst)
