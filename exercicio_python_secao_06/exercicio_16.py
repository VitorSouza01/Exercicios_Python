"""
15. Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares
de 1 até N em ordem decrescente.
"""
print("[DESCUBRA OS NÚMEROS ÍMPARES EM ORDEM DECRESCENTE]")
n = int(input("Digite um número inteiro positivo ímpar: "))

if n > 0 and (n % 2) == 1:
    for num in range(n, 0, -1):
        print(num)
else:
    print("\nValor informado inválido!")
