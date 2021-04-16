'''
    Exercício Python 076: Crie um programa que tenha uma tupla
    única com nomes de produtos e seus respectivos preços, na
    sequência. No final, mostre uma listagem de preços,
    organizando os dados em forma tabular.
'''

# Tupla
listagem = ('Lapís', 1.25,
            'Caneta', 1.75,
            'Borracha', 1.25,
            'Caderno', 15.99,
            'Tijolo Assado', 39.90,
            'Perna de Camelo', 1399.15)

# Cabeçalho
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

# Solução
for pos in range(0, len(listagem)): # para posição na distancia(0, tamanho(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')

    else:
        print(f'R$ {listagem[pos]:>7.2f}')

print('-'*40)
