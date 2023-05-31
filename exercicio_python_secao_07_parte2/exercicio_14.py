"""
14. Faça um programa para gerar automaticamente números entre 0 a 99 de uma cartela de bingo. Sabendo que cada cartela
deverá conter 5 linhas de 5 números, gere estes dados de modo a não ter números repetidos dentro das cartelas.
O programa deve exibir na tela a cartela gerada
"""

import random

numero = random.sample(range(0, 99), 25)
matriz = [numero[i::5] for i in range(5)]

print("Cartela de Bingo 5x5;")
for linha in matriz:
    print(linha)
