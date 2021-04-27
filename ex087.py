'''
    Exercício Python 087: Aprimore o desafio anterior,
    mostrando no final:
        
    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.
'''

# Listas
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Variáveis
s_pares = s_coluna = maior = 0

# Solução
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))

print('-=-'*13)
for linha in range(3):
    for coluna in range(3):
        print(f'    [{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            s_pares += matriz[linha][coluna]
    print()

print('-=-'*13)
print(f'A soma dos valores pares é: \033[34m{s_pares}\033[m')

for linha in range(3):
    s_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é: \033[34m{s_coluna}\033[m')

for coluna in range(3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

print(f'O maior valor da segunda linha é: \033[34m{maior}\033[m')
