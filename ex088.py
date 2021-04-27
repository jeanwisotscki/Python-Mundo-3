'''
    Exercício Python 088: Faça um programa que ajude
    um jogador da MEGA SENA a criar palpites. O
    programa vai perguntar quantos jogos serão
    gerados e vai sortear 6 números entre 1 e 60
    para cada jogo, cadastrando tudo em uma lista
    composta.
'''

# Bibliotecas
from random import sample
from time import sleep

# Variáveis e Listas
resultados = []

# Cabeçalho
print('---'*15)
print('{:^45}'.format('>>> JOGAR NA MEGA SENA <<<'))
print('---'*15)

jogos = int(input('{:^45}'.format('Digite quantos jogos quer sortear: ')))

print('---'*15)
print('{:^45}'.format(f'>>> SORTEANDO {jogos} JOGOS <<< '))
print('---'*15)
sleep(1)

# Solução
for c in range(jogos):
    r = sorted(sample(range(0, 61), 6))
    resultados.append(r[:])
    print('{:<45}'.format(f'Jogo {c+1}: {r}'))
    sleep(0.5)

print('{:^45}'.format(' === BOA SORTE ==='))
print('---'*15)
