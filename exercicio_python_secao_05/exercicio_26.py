"""
26. Leia a distâncoa em km e a quantidade de litros de gasolina consumidos por um carro
em um pecurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela
abaixo:

|---------------------------------|
|CONSUMO  |(Km/l)| MENSAGEM       |
|---------|------|----------------|
|menor que|   8  | Venda o carro! |
|entre    |8 e 14| Econômico!     |
|maior que|  12  | Super econômico|
|---------------------------------|
"""

print('-DESCUBRA O CONSUMO DE GASOLINA!')
quilometro = float(input('-Digite a distâncoa em quilômetros (Km):'))
litro = float(input('-Digite a quantidade de litros de gasolina colocado:'))

conta = quilometro / litro

if conta < 8:
    print('\nConsumo menor que 8 Km/l.')
    print(f'Seu consumo é:{conta} Km/l ')
    print('[VENDA O CARRO!]')
elif conta > 8 and conta < 14:
    print('\nConsumo entre 8 Km/l e 14 Kml.')
    print(f'Seu consumo é:{conta} Km/l ')
    print('[ECONÔMICO!]')
elif conta > 12:
    print('\nConsumo maior que 12 Kml.')
    print(f'Seu consumo é:{conta} Km/l ')
    print('[SUPER ECONÔMICO!]')



