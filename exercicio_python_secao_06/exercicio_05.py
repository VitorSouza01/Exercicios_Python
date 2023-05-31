"""
05. Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""
print("[Digite 10 valores e descubra a soma!]")
soma = 0
for n in range(1, 10 + 1):
    num = int(input(f"Digite o {n}° valor: "))
    soma = soma + num
print(f"A soma de todos os valores é {soma}")
