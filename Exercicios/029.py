'''
Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
'''
numero = int(input('Digite um núemro: '))
for i in range(1, 11):
    print(f'{numero} X {i} = {numero * i}')
