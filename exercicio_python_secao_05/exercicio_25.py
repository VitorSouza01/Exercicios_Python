"""
25. Calcule as raízes da equação de 2º grau;
Lembrando que: x= -b +- √△ / 2a
Onde: △ = b(2) - 4ac
E ax(2) + bx + c = 0 representa uma equação de 2º grau.

A variável 'a' tem que ser diferente de zero. Caso seja igual, imprima a mensagem;
"Não é equação de segundo grau".

*Se △ < 0 não existe real. Imprima a mensagem 'Não existe raiz'.
*Se △ = 0, existe uma raiz real. Imprima a raiz e a mensagem 'Raiz Única'.
*Se △ > 0, imprima as duas raizes reais.

fonte da respota: https://www.pythonprogressivo.net/2018/02/Programa-Acha-Raizes-Equacao-Segundo-2o-Grau.html
"""

import math

print('[ CALCULE AS RAÍZES DA EQUAÇÃO DE 2° GRAU]')
print('Forma: ax² + bx + c')

a = int(input('\nDigite o coeficiente a: '))

if (a == 0):
    print('△ = 0 - Raiz única.')
else:
    b = int(input('Coeficiente b: '))
    c = int(input('Coeficiente c: '))
    delta = b * b - (4 * a * c)

    if delta < 0:
        print('D△ < 0 - Não existe Raiz')
    elif delta == 0:
        raiz = -b / (2 * a)
        print('Delta=0 , raiz = ', raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print('Raizes: ', raiz1, ' e ', raiz2)

