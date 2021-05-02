'''
    Exercício Python 093: Crie um programa que gerencie o
    aproveitamento de um jogador de futebol. O programa
    vai ler o nome do jogador e quantas partidas ele
    jogou. Depois vai ler a quantidade de gols feitos em
    cada partida. No final, tudo isso será guardado em
    um dicionário, incluindo o total de gols feitos
    durante o campeonato.
'''

# Lista, Dicionários e Variáveis
jogador = {}
jogos = []
cont = 1
soma = 0

# Solução
jogador['gols'] = jogos
jogador['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(partidas):
    jogos.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
print()

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for v in jogos:
    print(f' => Na partida nº{cont}, fez {v} gols. ')
    cont += 1
    soma += v

print()
print(f'Foi um total de {soma} gols.')
