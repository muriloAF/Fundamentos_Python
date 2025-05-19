'''
Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média,
é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).
'''

nota1 = int(input('Digite a nota 1: '))
if nota1 < 0 and nota1 > 10:
    print('As notas devem ser de 0 até 10')
else:
    nota2 = int(input('Digite a nota 2: '))
if nota2 < 0 and nota2 > 10:
    print('As notas devem ser de 0 até 10')
else:
    nota3 = int(input('Digite a nota 3: '))
if nota3 < 0 and nota3 > 10:
    print('As notas devem ser de 0 até 10')
else:
    nota4 = int(input('Digite a nota 4: '))
if nota4 < 0 and nota4 > 10:
    print('As notas devem ser de 0 até 10')
else:
    nota5 = int(input('Digite a nota 5: '))
if nota5 < 0 and nota5 > 10:
    print('As notas devem ser de 0 até 10')

media = (nota1+nota2+nota3+nota4+nota5)/5

if media < 6:
    print(f'Sua média é insuficiente, tente novamente da próxima vez! média: {media}')
elif media < 7:
    print(f'Sua média é suficiente, ainda dá para melhorar! média: {media}')
elif media < 9:
    print(f'Sua média é boa, você está no caminho para a a perfeição! média: {media}')
else:
    print(f'Sua média está excelente, parabéns! média: {media}')