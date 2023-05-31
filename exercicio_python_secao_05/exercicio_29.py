"""
29. Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores doque 100.
Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: "Qual é a soma de A + B, onde A e B são
números aleatórios". Peça a respota. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou.
"""
import random

print("[  PROVA DE MATEMÁTICA  ]")
print("-RESPONDA AS PERGUNTAS;")
vlr1, vlr2 = random.randint(1,100), random.randint(1,100)
vlr3, vlr4 = random.randint(1,100), random.randint(1,100)
vlr5, vlr6 = random.randint(1,100), random.randint(1,100)
vlr7, vlr8 = random.randint(1,100), random.randint(1,100)
vlr9, vlr10 = random.randint(1,100), random.randint(1,100)

soma1 = vlr1 + vlr2
soma2 = vlr3 + vlr4
soma3 = vlr5 + vlr6
soma4 = vlr7 + vlr8
soma5 = vlr9 + vlr10

print(f"\n1° Quanto é {vlr1} + {vlr2}?")
rspt1 = int(input("Resposta:"))
print(f"2° Quanto é {vlr3} + {vlr4}?")
rspt2 = int(input("Resposta:"))
print(f"3° Quanto é {vlr5} + {vlr6}?")
rspt3 = int(input("Resposta:"))
print(f"4° Quanto é {vlr7} + {vlr8}?")
rspt4 = int(input("Resposta:"))
print(f"5° Quanto é {vlr9} + {vlr10}?")
rspt5 = int(input("Resposta:"))

certo = []
errado = []

if rspt1 == soma1:
    print(f'\nA 1° resposta  está Certa. {vlr1} + {vlr2} = {soma1}')
    certo.append(1)
else:
    print(f'\nA 1° resposta  está Errada! {vlr1} + {vlr2} = {soma1}')
    errado.append(0)

if rspt2 == soma2:
    print(f'A 2° resposta  está Certa. {vlr3} + {vlr4} = {soma2}')
    certo.append(1)
else:
    print(f'A 2° resposta  está Errada! {vlr3} + {vlr4} = {soma2}')
    errado.append(0)

if rspt3 == soma3:
    print(f'A 3° resposta  está Certa. {vlr5} + {vlr6} = {soma3}')
    certo.append(1)
else:
    print(f'A 3° resposta  está Errada! {vlr5} + {vlr6} = {soma3}')
    errado.append(0)

if rspt4 == soma4:
    print(f'A 4° resposta  está Certa. {vlr7} + {vlr8} = {soma4}')
    certo.append(1)
else:
    print(f'A 4° resposta  está Errada! {vlr7} + {vlr8} = {soma4}')
    errado.append(0)

if rspt5 == soma5:
    print(f'A 5° resposta  está Certa. {vlr9} + {vlr10} = {soma5}')
    certo.append(1)
else:
    print(f'A 5° resposta  está Errada! {vlr9} + {vlr10} = {soma5}')
    errado.append(0)

print(f'\n[Você Acertou {(certo.count(1))} Vezes].')

