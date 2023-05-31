"""
18. Faça um programa que leia um vetor de 10 números. Leia um número X. Conte os múltiplos de um número inteiro
inteiro X num vetor. Em seguida imprima o vetor na tela.
"""

vetor = []

for i in range(10):
  numero = int(input(f"Digite o {i+1}º número: "))
  vetor.append(numero)

x = int(input("\nDigite um número inteiro X: "))

multiplos = []
for numeros in vetor:
  if numeros % x == 0:
    multiplos.append(numeros)

print(f"\nOs múltiplos de {x} no vetor são: {multiplos}")

