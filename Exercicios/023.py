'''
Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.
'''

palavra = input('Digite uma palavra: ').strip().lower()[0]

if palavra in 'aeiou':
    print('É vogal')
else:
    print('É consoante')


