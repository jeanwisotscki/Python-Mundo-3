'''
    Exercício Python 074: Crie um programa que vai gerar
    cinco números aleatórios e colocar em uma tupla.
    Depois disso, mostre a listagem de números gerados
    e também indique o menor e o maior valor que estão
    na tupla.
'''

# Bibliotecas
from random import randint

# Tupla
valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

# Solução
print('Os valores sorteados foram: ', end='')

for n in valores:
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi: {max(valores)}')
print(f'O menor valor sorteado foi: {min(valores)}')

# opção 2
#print(f'{sorted(valores)[-1]} Foi o maior valor sorteado')
#print(f'{sorted(valores)[0]} Foi o menor valor sorteado')