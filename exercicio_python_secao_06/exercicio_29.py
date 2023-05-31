"""
29. Escreva um programa para calcular o valor da série, para 5 termos.
s = 0 + 1/2! + 2/4! + 3/6! + ...
"""
print("-Programa para calcular 5 termos")
print("Fórmula; s = 0 + 1/2! + 2/4! + 3/6! + ...")

n = 5
i1 = 0
i2 = 0
soma = 0

while i1 <= (n-1):
    i1 += 1
    i2 += 2
    soma = soma + i1 / i2
    print(f"{i1}/{i2}")
print(f"\nO valor conforme a fórmula é: {soma}.")
