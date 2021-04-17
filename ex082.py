'''
    Exercício Python 082: Crie um programa que vai ler vários
    números e colocar em uma lista. Depois disso, crie duas
    listas extras que vão conter apenas os valores pares e os
    valores ímpares digitados, respectivamente. Ao final,
    mostre o conteúdo das três listas geradas.
'''

# Listas
lista_par = []
lista_impar = []
lista = []

# Solução
while True:
    num = int(input('Digite um número: '))
    lista.append(num)

    if num % 2 == 0:
        lista_par.append(num)

    else:
        lista_impar.append(num)
    res = input('Quer continuar? [S/N] ').strip().upper()[0]

    while res not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()[0]

    if res == 'N':
        break

print('~=~'*12)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')
print('~=~'*12)
