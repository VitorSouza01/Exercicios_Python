"""
36. Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números
naturais e o quadrado da soma.
Ex; A soma dos quadrados dos dez primeiros números naturais é;

    1(2) + 2(2) + ... + 10(2) = 385

O quadrado da soma dos dez primeiros números naturais é;

    (1 + 2 + ... + 10)2 = 552 = 3025

A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é 3025 - 385 = 2640
"""
print("-Diferença da soma dos quadrado com o quadrado da soma de 1 até 100;")

#A soma dos quadrados
nmr1 = 0
sm1 = 0

for n in range(1, 100+1):
	nmr1 = n * n
	sm1 = sm1 + nmr1
print(f"\nA soma dos quadrado; {sm1}.")

#O quadrado da soma
nmr2 = 0
sm2 = 0

for n in range(1, 100+1):
	sm2 = sm2 + n
nmr2 = sm2 * sm2
print(f"O quadrado da soma; {nmr2}.")

#Diferença entre a soma dos quadrados e o quadrado da soma
dfrc = nmr2 - sm1

print(f"\nA diferença é; {dfrc}.")
