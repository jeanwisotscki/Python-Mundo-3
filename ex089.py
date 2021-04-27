'''
    Exercício Python 089: Crie um programa que leia
    nome e duas notas de vários alunos e guarde tudo
    em uma lista composta. No final, mostre um
    boletim contendo a média de cada um e permita
    que o usuário possa mostrar as notas de cada
    aluno individualmente.
'''

# Bibliotecas
from time import sleep

# Listas
ficha = []

# Solução
while True:
    nome = input('Nome: ').title()

    nota1 = float(input('Nota 1: '))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input('Nota inválida! Digite novamente: '))

    nota2 = float(input('Nota 2: '))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input('Nota inválida! Digite novamente: '))

    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    res = input('Quer continuar? [S/N] ').strip().upper()[0]
    while res not in 'SN':
        res = input('Caractere inválido! Digite novamente [S/N]: ').strip().upper()[0]
    if res in 'N':
        break

# Gerando a matriz
print('--'*15)
print(f'{"No.":<5}{"NOME":<12}{"MÉDIA":>10}')
print('--'*15)
for i, a in enumerate(ficha):
    print(f'{i:<5}{a[0]:<12}{a[2]:>9.1f}')

# Mostrar notas do aluno
while True:
    print('--'*15)
    opc = int(input('Quer mostrar as notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        sleep(1.5)
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print('<<< FIM DO PROGRAMA >>>')
