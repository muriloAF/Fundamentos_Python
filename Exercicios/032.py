'''
Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.
'''
n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva um outro número: '))

for i in range(n1, n2):
    if i%2 == 0:
        print(i)