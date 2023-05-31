""""
23. Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""
print("[Descubra os Divisores de um Número!]")

n = int(input("Digite um valor de um número positvo: "))

if n >= 1:
    for i in range(1,n):
        if n % i == 0:
            print(i)

else:
    print("\nO Valor Digitado é Inválido!")
