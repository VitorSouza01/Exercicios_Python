"""
11. Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais
de 0 até N em ordem crescente.
"""
print("[DESCUBRA OS NÚMEROS NATURAIS EM ORDEM CRESCENTE]")
n = int(input("Digite um número inteiro positivo: "))
if n > 0:
    for num in range(0, n+1):
        print(num)
else:
    print("\nValor informado inválido!")

