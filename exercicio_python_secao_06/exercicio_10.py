""""
10. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
"""
print("-A soma dos 50 primeiros números pares.")
soma = 0

for num in range(2, 102, 2):
    print(num)
    soma = soma + num
print(f"A soma dos 50 primeiros números pares são; {soma}")

