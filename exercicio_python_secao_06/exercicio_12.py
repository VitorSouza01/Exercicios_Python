"""
12. Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais
de 0 até N em ordem decrescente.
"""
print("[DESCUBRA OS NÚMEROS NATURAIS EM ORDEM DECRESCENTE]")
n = int(input("Digite um número inteiro positivo: "))
if n > 0:
    for num in range(n, -1, -1):
        print(num)
else:
    print("\nValor informado inválido!")
