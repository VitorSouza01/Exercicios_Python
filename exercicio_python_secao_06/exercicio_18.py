"""
18. Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior
número foi lido. A quantidade de números a serem lidos deve ser fornecido pelo usuário.
"""
quantidade = int(input("-Digite a quantidade de vezes que o algoritmo vai ler os números: "))
n = 0
lista = []

while n < quantidade:
    num = int(input('Digite um número: '))
    n += 1
    lista.append(num)

maior = max(lista)
print(f'\nO maior valor é {maior} e ele foi lido {lista.count(maior)} vezes')

