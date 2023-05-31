"""
38. Faça um programa que calcule o terno pitagoórico a, b, c para o qual a + b + c = 1000.
Um terno pitagórico é um conjunto de três números naturais a, b, c, para qual,

	a² + b² = c²

Por exemplo;
	3² + 4² = 9 + 16 = 25 = 5²
"""
print("Programa para calcular o terno pitagórico!\n")

c = 997
terno = True

while terno:
    for b in range(2, 1000-c):
        for a in range(1, b):
            if a + b + c == 1000 and (a*a) + (b*b) == (c*c):
                terno = False
                ptgr = a * b * c

                print(f"Valor de A:{a}.")
                print(f"Valor de B:{b}.")
                print(f"Valor de C:{c}.")
                print(f"O terno pitagórico é; {ptgr}.")

                break

    c -= 1


