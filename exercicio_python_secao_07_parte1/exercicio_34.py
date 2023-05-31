"""
34. Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor. Os dados deverão ser armazenados
no vetor na ordem que forem sendo lidos, sendo que caso o usuário digite um número que já foi digitado anteriormente,
o programa deverá pedir para ele digitar outro número. Note que cada valor digitado pelo usuário deve ser
pesquisado no vetor, verificando se ele existe entre os números que já foram fornecidos. Exibit na tela o vetor
final que foi digitado.
"""

vetor = []

for i in range(10):
    while True:
        numero = int(input(f"Digite o valor do {i + 1}º número (o número não pode ser repetido!): "))
        if numero not in vetor:
            vetor.append(numero)
            break

        else:
            print("\n[NÚMERO DIGITADO INVALIDO!]")
            print(f"O número {numero} não pode ser repetido!\n")

print(f"\nO Vetor completo é: {vetor}.")
