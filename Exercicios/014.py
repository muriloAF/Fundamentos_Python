'''
Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.
'''

numero= float(input('Digite um número qualquer número: '))

if numero < 0.0:
    print('O número é negativo')
elif numero == 0:
    print('O número é nulo')
else:
    print('O número é positivo')

