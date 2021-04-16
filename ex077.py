##############################################################
#                    SEPARADOR DE VOGAIS                     #
##############################################################

'''
    Exercício Python 077: Crie um programa que tenha uma tupla
    com várias palavras (não usar acentos). Depois disso,
    você deve mostrar, para cada palavra, quais são as suas
    vogais.
'''

# Tuplas:
palavras = ('APRENDER', 'PROGRAMAR', 'AMAR',
            'ODIAR', 'ESCREVER', 'PYTHON',
            'CURSO', 'TRABALHAR', 'FUTURO', 'SKYBYRT')
vogais = ('A', 'E', 'I', 'O', 'U')

# Solução
for palavra in palavras: # PARA A palavra NA TUPLA(palavras):
    print(f'\nNa palavra {palavra} temos: ', end='') # ESCREVA A palavra

    for letras in palavra: # PARA AS letras NA palavra:
        if letras in vogais: # SE AS letras ESTIVEREM NAS vogais:
            print(f'\033[34m{letras}\033[m', end=' ') # ESCREVA AS letras
