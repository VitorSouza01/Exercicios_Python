"""
15. Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares
de 1 até N em ordem crescente.
"""
print("[DESCUBRA OS NÚMEROS ÍMPARES EM ORDEM CRESCENTE]")
n = int(input("Digite um número inteiro positivo ímpar: "))

if n > 0 and (n % 2) == 1:
    for num in range(1, n+1):
        print(num)
else:
    print("\nValor informado inválido!")

