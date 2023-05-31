"""
25. Faça um programa que some todos os números naturais abaixo de 1000 e são múltiplos de 3 ou 5.
"""
print("[SOMA DE TODOS OS NÚMEROS NATURAIS ABAIXO DE 1000 E MÚLTIPLOS DE 3.]")
soma3 = 0
soma5 = 0

for n1 in range(0, 1000+1):
    if n1 % 3 == 0:
        print(n1)
        soma3 = soma3 + n1

print(f"\nA soma de todos os números naturais abaixo de 1000 múltiplo de 3 é; [{soma3}].")

for n2 in range(0, 1000+1):
    if n2 % 5 == 0:
        print(n2)
        soma5 = soma5 + n2

print(f"\nA soma de todos os números naturais abaixo de 1000 múltiplo de 5 é; [{soma5}].")
