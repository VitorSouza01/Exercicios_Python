""""
39. Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário.
Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.
"""
print("[Descubra A Área De Um Triângulo]")

base = float(input("\n-Digite o valor da base: "))
altura = float(input("-Digite o valor da altura: "))

if base > 1 and altura > 1:

    area = (base * altura) / 2
    print(f"\nA Área do Triângulo é: {area}.")

else:
    print("\n[Os Valores Informados São Inválidos!]")
