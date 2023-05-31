"""
14. Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares
de 0 até N em ordem decrescente.
"""
print("[DESCUBRA OS NÚMEROS PARES EM ORDEM DECRESCENTE]")
n = int(input("Digite um número inteiro positivo par: "))

if n > 0 and (n % 2) == 0:
    for num in range(n, -1, -1):
        print(num)
else:
    print("\nValor informado inválido!")
