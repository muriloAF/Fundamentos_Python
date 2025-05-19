'''
Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.
'''

numero = float(input('Digite um número: '))

if numero >= 0:
    if numero <= 10:
        print('O número esta entre 0 e 10')
    elif numero > 10:

        if numero <= 20:
            print('O número esta entre 10 e 20')
        else:
            print('O núemro é maior que 20')
else:
    print('O número é menor que 0')
