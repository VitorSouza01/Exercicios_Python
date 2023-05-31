"""
30. Faça um programa que receba trêS números e mostre-os em ordem crescente.
"""
print("[DESCUBRA A ORDEM CRESCENTE DOS 3 NÚMEROS INTEIROS!]")

numero1 = int(input("\nDigite o primeiro número:"))
numero2 = int(input("\Digite o segundo número:"))
numero3 = int(input("\Digite o terceiro número:"))

lista = [numero1, numero2, numero3]
lista.sort()

print(f"\nA ordem dos três crescente é: {(lista)}.")




