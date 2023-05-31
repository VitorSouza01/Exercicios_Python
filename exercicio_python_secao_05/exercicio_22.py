"""
22. Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
As condições para aposentadoria são;
* Ter pelo menos 65 anos.
* Ou ter trabalhado pelo menos 30 anos.
* Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""

print('-- Descubra se você pode se aposentar! --')
print('\n- Condições para aposentar;')
print('* Ter pelo menos 65 anos!')
print('* Ou ter trabalhado pelo menos 30 anos!')
print('* Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos!')

nome = str(input('\nDigite o seu nome:'))
idade = int(input('Digite a sua idade:'))
anos_trabalho = int(input('Digite por quantos anos está trabalhando:'))

if idade >= 65:
    print(f'\nParabéns {nome}! Você pode se aposentar!')
    print('Você tem pelo menos 65 anos.')
elif anos_trabalho >= 30:
    print(f'\nParabéns {nome}! Você pode se aposentar!')
    print('Você tem trabalhado pelo menos 30 anos.')
elif idade >= 60 and anos_trabalho >= 25:
    print(f'\nParabéns {nome}! Você pode se aposentar!')
    print('Você tem pelo menos 60 anos e está trabalhado pelo menos 30 anos.')
else:
    print(f'\n{nome} infelizmente no momento você não pode se aposentar.')
