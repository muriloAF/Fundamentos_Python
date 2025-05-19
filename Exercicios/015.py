'''
Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar
'''

numero = int(input('Digite um número qualquer: '))
resto = (numero % 2)

if resto == 0:
    print('O número é par')

else:
    print('O número é ímpar')