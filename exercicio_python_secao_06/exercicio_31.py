"""
31. Faça um programa que calcule e escreva o valor de S;
    S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
"""
print("-Calcule e escreva o valor de S")
print("Fórmula; S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50")

n = 50
i1 = 1
i2 = 1
soma = 0

while i2 <= n:
    soma = soma + i1 / i2
    print(f"{i1}/{i2}")
    i1 += 2
    i2 += 1
print(f"\nO valor conforme a fórmula é: {soma}.")