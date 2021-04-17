'''
    Exercício Python 079: Crie um programa onde o usuário
    possa digitar vários valores numéricos e cadastre-os
    em uma lista. Caso o número já exista lá dentro, ele
    não será adicionado. No final, serão exibidos todos
    os valores únicos digitados, em ordem crescente.
'''

lista = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    if lista.count(valor) == 2: # pode ser feito com 'not in'
        print('Valor duplicado! Não adicionado.')
        lista.pop()

    else:
        print('Valor adicionado!')

    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]

    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N] ').strip().upper()[0]

    if continuar in 'N':
        break

lista.sort()
print('~=~'*15)
print(f'Você digitou os valores {lista}')
print('~=~'*15)
