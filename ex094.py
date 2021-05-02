'''
    Exercício Python 094: Crie um programa que leia
    nome, sexo e idade de várias pessoas, guardando
    os dados de cada pessoa em um dicionário e
    todos os dicionários em uma lista. No final,
    mostre:
    A) Quantas pessoas foram cadastradas
    B) A média de idade
    C) Uma lista com as mulheres
    D) Uma lista de pessoas com idade acima da média
'''

# Dicionários, listas e variáveis
pessoas = {}
lista = []
mulheres = []
acima = []
media = soma = 0

# Solução
while True:
    pessoas['nome'] = input('Nome: ')
    pessoas['sexo'] = input('Sexo [M/F]: ').upper().strip()[0]

    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas['nome'])
    while pessoas['sexo'] not in 'MF':
        pessoas['sexo'] = input('Por favor, digite apenas "M" ou "F": ').upper().strip()[0]

    pessoas['idade'] = int(input('Idade: '))
    if pessoas['idade'] > 0:
        soma += pessoas['idade']

    lista.append(pessoas.copy())
    res = input('Quer continuar? [S/N] ').upper().strip()[0]
    while res not in 'SN':
        res = input('Por favor, digite apenas "S" ou "N": ').upper().strip()[0]

    if res == 'N':
        break

media = soma / len(lista)
for p in lista:
    if p['idade'] > media:
        acima.append(p)

# Exibindo os resultados
print('-='*20)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade do grupo é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}')
print(f'D) Lista de pessoas que estão acima da média de idade: {acima}')
print('-='*20)
print('>>> PROGRAMA FINALIZADO <<<')
