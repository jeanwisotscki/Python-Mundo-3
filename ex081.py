'''
    Exercício Python 081: Crie um programa que vai ler vários
    números e colocar em uma lista. Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []

while True:
    lista.append(int(input('Digite um VALOR: ')))
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    while resp not in 'SN':
        resp = input('\033[31mOpção inválida.\033[m Deseja continuar? [S/N] ').strip().upper()[0]

    if resp == 'N':
        break

lista.sort(reverse=True)

print('~=~'*14)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')

if 5 not in lista:
    print('O valor "5" não faz parte da lista.')

else:
    print('O valor "5" faz parte da lista.')
print('~=~'*14)
