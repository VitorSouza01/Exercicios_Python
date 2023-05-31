"""
55. Escreva um programa que leia um número inteiro não negativo n e imprima a soma dos n primeiros
números primos
"""
n = int(input('-Digite um número inteiro positivo: '))

soma = 0
conta = 0
num = 2

while conta < n:

    cdg = True
    for i in range(2, num):
        if num % i == 0:
           cdg = False
           break

    if cdg:
        print(num)
        soma += num
        conta += 1
    num += 1

print(f"\n-A soma dos {n} primeiros números primos são; {soma}.")
