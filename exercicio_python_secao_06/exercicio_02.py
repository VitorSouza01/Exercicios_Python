"""
02. Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar
a estrutura de repetição for, a segunda while, e a terceira do while.
"""
print("[1 até 100 - Usando For, While e Do While!]")
print("-Usando o 'For';")
for numero in range (1,101):
    print(numero)

print("\n-Usando o 'While';")
numero = 1
while numero < 101:
    print(numero)
    numero = numero + 1


print("\n-Usando o 'Do While';")
print("Obs; Não existe 'Do While' em Python!")