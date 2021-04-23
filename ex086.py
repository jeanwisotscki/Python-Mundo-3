'''
    Exercício Python 086: Crie um programa que declare
    uma matriz de dimensão 3×3 e preencha com valores
    lidos pelo teclado. No final, mostre a matriz na
    tela, com a formatação correta.
'''

# Listas
matriz = [[], [], []]

# Solução
for i in range(3):
    for c in range(3):
        matriz[i].append(int(input(f'Digite um número para posição [{i}, {c}]: ')))
print('~='*20)

for i in range(3):
    for c in range(3):
        print(f'    [{matriz[i][c]:^5}] ', end='')
    print()
print('~='*20)
