'''
    Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros
    colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem
    de colocação. Depois mostre:

    a) Os 5 primeiros times.

    b) Os últimos 4 colocados.

    c) Times em ordem alfabética.

    d) Em que posição está o time da Chapecoense.
'''

# Tupla
serieA = ('Flamengo', 'Internacional', 'Atletico-MG', 'Fluminense',
          'Sao Paulo', 'Gremio', 'Palmeiras', 'Santos', 'Atletico-PR',
          'Corinthians', 'Bragantino')

# Solução
print('-=-'*30)
print(f'Lista de times do Brasileirão Série A: {serieA}')

print('-=-'*30)
print(f'Os 5 primeiros são: {serieA[0:5]}')

print('-=-'*30)
print(f'Os 4 últimos são: {serieA[-4:]}')

print('-=-'*30)
print(f'Lista em ordem alfabética: ', end='')
print(sorted(serieA))

print('-=-'*30)
print(f'O time do Palmeiras está na {serieA.index("Palmeiras")+1}ª posição do ranking.')
print('-=-'*30)
