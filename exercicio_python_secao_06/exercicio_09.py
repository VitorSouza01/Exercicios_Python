""""
09. Faça um programa que leia um número inteiro n e depois imprima os n primeiros números
naturais ímpares
"""
print("-Escreva um número inteiro e saiba os primeiros números ímpares.")
n = int(input("Digite um número inteiro: "))
print(f"\nOs primeiros números naturais ímpares são;")
for n in range(1, n, 2):
    print(n)



