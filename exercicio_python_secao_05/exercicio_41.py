"""
41. Faça um algoritmo que calcule IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:

IMC         |   CLASSIFICAÇÃO              |
< 18.5      | Abaixo do peso               |
18.6 - 24.9 | Saudável                     |
25.0 - 29.9 | Peso em excesso              |
30.0 - 34.9 | Obesidade Grau I             |
35.0 - 39.9 | Obesidade Grau II (severa)   |
> 40        | Obesidade Grau III (mórbida) |
"""
print("[CALCULO DE IMC]")

peso = int(input('\nInforme o seu peso (Kg):'))
altura = float(input('Informe a sua altura (Metro):'))

imc = str(peso / (altura * altura))
imc = imc[0:4]

if float(imc) <= 18.5:
    print(f"\nO seu IMC é: [{imc}]. Você está Abaixo do Peso!")

elif 18.6 <= float(imc) <= 24.9:
    print(f"\nO seu IMC é: [{imc}]. Você está Saudável!")

elif 25.0 <= float(imc) <= 29.9:
    print(f"\nO seu IMC é: [{imc}]. Você está com Peso em Excesso!")

elif 30.0 <= float(imc) <= 34.9:
    print(f"\nO seu IMC é: [{imc}]. Você está com Obesidade Grau I!")

elif 35.0 <= float(imc) <= 39.9:
    print(f"\nO seu IMC é: [{imc}]. Você está com Obesidade Grau II (Severa)!")

elif float(imc) > 40:
    print(f"\nO seu IMC é: [{imc}]. Você está com Obesidade Grau III (Mórbida)!")
