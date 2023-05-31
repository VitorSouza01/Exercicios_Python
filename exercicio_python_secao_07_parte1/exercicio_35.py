"""
35. Faça um programa que leia dois números A e B (positivos menores que 10000) e:
    * Crie um vetor onde cada posição é um algarismo do número. A primeira posição é o algarismo menos significativo;
    * Crie um vetor que seja a soma de A e B, mas faça-o usando apenas os vetores construídos anteriormente.

Dica: some as posições correspondentes. Se a soma ultrapassar 10, subtraia 10 do resultado e some 1 à próxima posição.
"""

valor_a = int(input("Digite o valor positivo do Número A: "))
valor_b = int(input("Digite o valor positivo do Número B: "))

vetor_valor_a = [int(c) for c in str(valor_a)][::-1]
vetor_valor_b = [int(c) for c in str(valor_b)][::-1]

while len(vetor_valor_a) < len(vetor_valor_b):
    vetor_valor_a.append(0)
while len(vetor_valor_b) < len(vetor_valor_a):
    vetor_valor_b.append(0)

vetor_soma = []
carry = 0

for i in range(len(vetor_valor_a)):
    soma = vetor_valor_a[i] + vetor_valor_b[i] + carry
    carry = 0
    if soma >= 10:
        soma -= 10
        carry = 1
    vetor_soma.append(soma)
if carry == 1:
    vetor_soma.append(1)

print("O Vetor da Soma do Vetor A:", valor_a, "e do Vetor B:", valor_b, "é: ",
      "".join(str(c) for c in vetor_soma[::-1]))
