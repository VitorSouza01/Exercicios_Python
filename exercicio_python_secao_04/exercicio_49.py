"""
49. Faça um programa para leia o hórario (hora, minuto e segundo) de inicio e a duração, em
segundos, de uma experiência biológica. O programa deve resultar, com o novo horário
(hora, minuto e segundo) do termino da mesma.
"""
#Código de respota; https://brainly.com.br/tarefa/38885954?cb=1655247956929

print('[ DESCUBRA A DURAÇÃO DO EVENTO! ]')

print('\nPreencha os campos abaixo com o horário atual')
horas = int(input('Horas:'))
minutos = int(input('Minutos:'))
segundos = int(input('Segundos:'))
duracao = int(input('Duração do evento em segundos:'))

segundos_final = (segundos + duracao) % 60
minutos_final = (minutos + (segundos + duracao) // 60) % 60
horas_final = (horas + (minutos + (segundos + duracao) // 60) // 60) % 24

print(f'\nO fim do evento se dará àS {horas_final}h {minutos_final}min e {segundos_final}segundos.')

