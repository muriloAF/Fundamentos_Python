'''
Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma
'''
soma = 0
for i in range(1, 11):
    n = int(input(f'Digite o {i}° número: '))
    if n%2 == 0:
        soma += n
print(soma)
