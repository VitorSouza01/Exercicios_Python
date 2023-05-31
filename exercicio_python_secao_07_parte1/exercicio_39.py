"""
39. Escreva um programa que leia um número inteiro positivo N e em seguida imprima N linhas do chamado
Triangulo de Pascal:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""

numero = int(input("Digite um número inteiro positivo: "))
print("\nTriandulo Pascal:")
for i in range(numero):
    print(''*(numero-i), end='')
    print(''.join(map(str, str(11**i))))
