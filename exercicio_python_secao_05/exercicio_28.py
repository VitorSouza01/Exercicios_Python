"""
28. Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:
(a)Geométrica
(b)Ponderada
(c)Harmônica
(d)Aritmética
"""
import statistics

print('[CALCULANDO AS OPERAÇÕES]')

print('\n-TIPOS DE OPERAÇÕES;')
print('(a)Geométrica')
print('(b)Ponderada')
print('(c)Harmônica')
print('(d)Aritmética')

nmr1 = int(input("\nDigite o primeiro número inteiro positivo:"))
nmr2 = int(input("Digite o segundo número inteiro positivo:"))
nmr3 = int(input("Digite o terceiro número inteiro positivo:"))
oprc = str(input("Digite uma letra que indica uma das 4 operações mostrado anteriormente:"))

hmnc = nmr1, nmr2, nmr3

if nmr1 > 0 and nmr2 > 0 and nmr3 > 0:
    if oprc == "a" or oprc == "D":
        print(f"\n-A Operação Geométrica ente os números {nmr1},{nmr2},{nmr3} é; [{(((nmr1)*(nmr2)*(nmr3))**(1/3))}].")

    elif oprc == "b" or oprc == "B":
        print(f"\n-A Operação Ponderada ente os números {nmr1},{nmr2},{nmr3} é; "
              f"[{(((1*nmr1)+(2*nmr2)+(3*nmr3))/(1+2+3))}].")

    elif oprc == "c" or oprc == "C":
        print(f"\n-A Operação Harmônica ente os números {nmr1},{nmr2},{nmr3} é; [{statistics.harmonic_mean(hmnc)}].")

    elif oprc == "d" or oprc == "D":
        print(f"\n-A Operação Aritmética ente os números {nmr1},{nmr2},{nmr3} é; [{((nmr1+nmr2+nmr3)/3)}].")
else:
    print("\n-Número Inválido! Digite um número inteiro positivo.")




