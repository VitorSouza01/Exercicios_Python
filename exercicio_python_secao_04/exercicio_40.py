"""
40. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa
que solicite o número de dias do trabalhados pelo encanador e imprima a
quantia líquida que deverá ser paga, sabendo-se que são descontados
8% para imposto de renda.
"""
diaria = int(input('Quantos dias o encanador trabalhou na empresa?'))

salario = (diaria * 30)
imposto = (8 * salario) / 100
valor_final = salario - imposto

print(f'\nO Encanador trabalhou por {diaria} dias, e irá receber R$[{valor_final}]. ')
print('*Esse valor é devido aos 8% de desconto devido ao imposto de renda.')

