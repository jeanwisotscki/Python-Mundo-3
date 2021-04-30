'''
    Exercício Python 092: Crie um programa que leia
    nome, ano de nascimento e carteira de trabalho
    e cadastre-o (com idade) em um dicionário. Se
    por acaso a CTPS for diferente de ZERO, o
    dicionário receberá também o ano de contratação
    e o salário. Calcule e acrescente, além da
    idade, com quantos anos a pessoa vai se aposentar.
'''

# Bibliotecas
from datetime import date

# Variáveis e Dicionários
atual = date.today().year
dados = {}

# Recebendo os dados
print('~='*20)
dados['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
dados['ctps'] = int(input('Carteira de Trabalho ("0" SE NÃO TIVER): '))

if dados['ctps'] != 0:
    dados['cont'] = int(input('Ano de Contratação: '))
    dados['sal'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['cont'] + 35) - nasc
    print('~='*20)

    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {idade} anos')
    print(f'Número CTPS: {dados["ctps"]}')
    print(f'Ano de contratação: {dados["cont"]}')
    print(f'Salário: R${dados["sal"]:.2f}')
    print(f'{dados["nome"]} vai se aposentar com {dados["aposentadoria"]} anos')

else:
    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {idade} anos')

print('~='*20)
