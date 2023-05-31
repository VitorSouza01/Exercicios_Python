"""
46. Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar
qual o número foi gerado, a cada tentativa o programa deverá informar se o chute é menor ou
maior que o número gerado. O programa acaba quando o usuário acerta o número gerado.
O programa deve informar em quantas tentativas o número foi descoberto.
"""
import random
print("-Acerte o número de 1 até 1000!")

x = random.randrange(1,1000)

cdg = True
loop = 0

while cdg:

    loop += 1

    chute = int(input("\n-Chute um número: "))

    if chute < x:
        print("\n[Errou! Tente Novamente!]")
        print(f"O número é maior que {chute}.")

    elif chute > x:
        print("\n[Errou! Tente Novamente!]")
        print(f"O número é menor que {chute}.")

    else:
        print("\n[Parabéns! Você Acertou!]")
        print(f"O número era; {x}.")
        print(f"[Você tentou {loop} vezes até acertar!]")

        cdg = False
