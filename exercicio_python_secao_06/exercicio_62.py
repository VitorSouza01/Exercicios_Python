"""
62. Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro, cinco, então há
2 + 4 + 4 + 6 + 5 = 22 letras usadas no total. Faça um programa que conte quantas letras
seriam utilizadas se todos os números de 1 a 1000 (mil) fossem escritos em palavras.
OBS: Não conte espaços ou hifens.
"""
print("-Descubra quantas letras seriam utilizadas de 1 a 1000 escritas em palavras.")

# soma do número 1 até o 99
sm_nmr_1_99: int

# soma do número 100 até o 1000
sm_nmr_100_1000: int


# 1 até 9
n1_n9 = [2, 4, 4, 6, 5, 4, 4, 4, 4]

# 10 até 19
n10_n19 = [3, 4, 4, 5, 8, 6, 9, 9, 7, 8]

# 20 até 29
n20_n29 = 5 + (5 * 9) + (sum(n1_n9))

# 30 até 39
n30_n39 = 6 + (6 * 9) + (sum(n1_n9))

# 40 até 49
n40_n49 = 8 + (8 * 9) + (sum(n1_n9))

# 50 até 59
n50_n59 = 9 + (9 * 9) + (sum(n1_n9))

# 60 até 69
n60_n69 = 8 + (8 * 9) + (sum(n1_n9))

# 70 até 79
n70_n79 = 7 + (7 * 9) + (sum(n1_n9))

# 80 até 89
n80_n89 = 7 + (7 * 9) + (sum(n1_n9))

# 90 até 99
n90_n99 = 7 + (7 * 9) + (sum(n1_n9))

# 72 é os 'e'
sm_nmr_1_99 = sum(n1_n9 + n10_n19) + \
              (n20_n29 + n30_n39 + n40_n49 + n50_n59 + n60_n69 + n70_n79 + n80_n89 + n90_n99) + 72


# 99 solto é os 'e'
# 100 até 199
n100_n199 = 3 + (5 * 99) + (sm_nmr_1_99 + 99)

# 200 até 299
n200_n299 = 8 + (8 * 99) + (sm_nmr_1_99 + 99)

# 300 até 399
n300_n399 = 9 + (9 * 99) + (sm_nmr_1_99 + 99)

# 400 até 499
n400_n499 = 12 + (12 * 99) + (sm_nmr_1_99 + 99)

# 500 até 599
n500_n599 = 10 + (10 * 99) + (sm_nmr_1_99 + 99)

# 600 até 699
n600_n699 = 10 + (10 * 99) + (sm_nmr_1_99 + 99)

# 700 até 799
n700_n799 = 10 + (10 * 99) + (sm_nmr_1_99 + 99)

# 800 até 899
n800_n899 = 10 + (10 * 99) + (sm_nmr_1_99 + 99)

# 900 até 999
n900_n999 = 10 + (10 * 99) + (sm_nmr_1_99 + 99)

# 1000
n1000 = 3

sm_nmr_100_1000 = (n100_n199 + n200_n299 + n300_n399 + n400_n499 + n500_n599 +
                   n600_n699 + n700_n799 + n800_n899 + n900_n999 + n1000)

print(f"\n-Seriam utilizadas no total de 1 a 1000 escritas em palavras [{sm_nmr_100_1000}] letras.")
