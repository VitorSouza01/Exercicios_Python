"""
13. Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares
de 0 até N em ordem crescente.
"""
print("[DESCUBRA OS NÚMEROS PARES EM ORDEM CRESCENTE]")
n = int(input("Digite um número inteiro positivo par: "))
par = n % 2

if n > 0 and par == 0:
    for num in range(0, n+1):
        print(num)
else:
    print("\nValor informado inválido!")

