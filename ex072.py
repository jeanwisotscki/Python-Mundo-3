'''
    Exercício Python 72: Crie um programa que tenha uma dupla
    totalmente preenchida com uma contagem por extenso, de
    zero até vinte. Seu programa deverá ler um número pelo
    teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

# Tupla
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Solução
while True:
    num = int(input('Digite um número de 0 a 20: '))

    while num > 20 or num < 0:
        num = int(input('Número Inválido! Digite um número de 0 a 20: '))

    print(f'Você digitou o número \033[34m{extenso[num]}\033[m')
    resp = input('Você quer continuar? [\033[32mS\033[m/\033[31mN\033[m] ').strip().upper()[0]

    while resp not in 'N':
        num = int(input('Digite um número de 0 a 20: '))

        while num > 20 or num < 0:
            num = int(input('Número Inválido! Digite um número de 0 a 20: '))

        print(f'Você digitou o número \033[34m{extenso[num]}\033[m')
        resp = input('Você quer continuar? [\033[32mS\033[m/\033[31mN\033[m] ').strip().upper()[0]

    if resp == 'N':
        break

print('Fim')
