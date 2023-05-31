"""
17. Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais.
"""
print("[DESCUBRA A SOMA DOS PRIMEIROS NÚMEROS NATURAIS]")
n = int(input("Digite um número inteiro positivo: "))
soma = 0

if n > 0:
    for num in range(0, n+1):
        soma = soma + num
    print(f"\nA soma dos primeiros números naturais é; {soma}.")
else:
    print("\nValor informado inválido!")

