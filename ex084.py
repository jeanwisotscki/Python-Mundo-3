'''
    Exercício Python 084: Faça um programa que leia nome e peso
    de várias pessoas, guardando tudo em uma lista. No final,
    mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
'''

# Listas e Variáveis
lista = []
dados = []
mai = men = 0

# Solução
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))

    if len(lista) == 0:
        mai = men = dados[1]

    else:
        if dados[1] > mai:
            mai = dados[1]

        if dados[1] < men:
            men = dados[1]

    lista.append(dados[:])
    dados.clear()
    
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]

    while resp not in 'SN':
        resp = input('RESPOSTA INVÁLIDA! Continuar? [S/N] ').strip().upper()[0]

    if resp in 'N':
        break

print('~=~'*13)
print(f'Ao todo, {len(lista)} pessoas foram cadastradas.')
print(f'O maior peso foi {mai:.2f}kg. Peso de: ', end='')

for p in lista:
    if p[1] == mai:
        print(f'"{p[0]}" ', end='')

print(f'\nO menor peso foi {men:.2f}kg. Peso de: ', end='')

for p in lista:
    if p[1] == men:
        print(f'"{p[0]}" ', end='')

print()
print('~=~'*13)
