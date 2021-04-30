'''
    Exercício Python 091: Crie um programa onde 4 jogadores
    joguem um dado e tenham resultados aleatórios. Guarde
    esses resultados em um dicionário em Python. No final,
    coloque esse dicionário em ordem, sabendo que o vencedor
    tirou o maior número no dado.
'''

# Bibliotecas
from random import randint
from time import sleep
from operator import itemgetter

# Dicionário
jogadores = {'Player 1': randint(1, 6),
             'Player 2': randint(1, 6),
             'Player 3': randint(1, 6),
             'Player 4': randint(1, 6)}

# Variáveis
seq = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
cont = 1

# Solução
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'   O {k} jogou {v} ')
    sleep(0.5)
print()

print('Ranking dos jogadores:')
sleep(0.5)
for k, v in seq:
    print(f'   {cont}º Lugar: {k} com {v}', end=' ')
    cont += 1
    sleep(0.5)
    print()

print()
sleep(0.8)
print('<<< PROGRAMA FINALIZADO >>>')
