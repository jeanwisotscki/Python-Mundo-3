'''
    Exercício Python 090: Faça um programa que leia nome e
    média de um aluno, guardando também a situação em um
    dicionário. No final, mostre o conteúdo da estrutura
    na tela.
'''

print('~='*16)
aluno = {'nome': input('Nome: ')}
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

print('~='*16)
print(f' - O nome do aluno é {aluno["nome"]}')
print(f' - A média do aluno é {aluno["media"]}')

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aluno Aprovado!'

elif aluno['media'] >= 5 < 7:
    aluno['situacao'] = 'Aluno de Recuperação!'

else:
    aluno['situacao'] = 'Aluno Reprovado!'

print(f" - {aluno['situacao']}")
print('~='*16)
