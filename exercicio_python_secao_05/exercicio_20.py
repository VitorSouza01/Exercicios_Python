"""
20. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
    * O comprimento de cada lado de um triângualo é menor do que a soma dos outros dois lados.
    * Chama-se equilátero o triângulo que tem três lados iguais.
    * Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    * Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""
print('- Verifique se três valores podem ser valores de lados de um triângulo, e qual é o tipo de triângulo!')
a = float(input('\n[Digite o valor A]:'))
b = float(input('[Digite o valor B]:'))
c = float(input('[Digite o valor C]:'))


if a < (b+c) and b < (a+c) and c < (a+b):
    if a == b and a == c and b == c:
        print('\nOs valores são válidos para um triângulo!')
        print('Esse triângulo é denominado de "Triângulo Equilátero" (Possui três lados iguais).')
    elif ((a != b and c) and b == c) or ((b != a and c) and a == c) or ((c != a and b) and a == b):
        print('\nOs valores são válidos para um triângulo!')
        print('Esse triângulo é denominado de "Triângulo Isósceles" (Possui dois lados iguais).')
    elif a != b and a != c and b != c:
        print('\nOs valores são válidos para um triângulo!')
        print('Esse triângulo é denominado de "Triângulo Escaleno" (Possui os três lados diferentes)')
else:
    print('\nOs valores não são válidos para um triângulo!')
