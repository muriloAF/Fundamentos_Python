'''
Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).
'''
numero = int(input('Digite um número de 1 a 7: '))
if numero < 1 or numero > 7:
    print('O número não corresponde ao requisitado')
else:
    if numero == 1:
        print('O dia da semana é Domingo')
    elif numero == 2:
        print('O dia da semana é Segunda')
    elif numero == 3:
        print('O dia da semana é Terça')
    elif numero == 4:
        print('O dia da semana é Quarta')
    elif numero == 5:
        print('O dia da semana é Quinta')
    elif numero == 6:
        print('O dia da semana é Sexta')
    elif numero == 7:
        print('O dia da semana é Sábado')


