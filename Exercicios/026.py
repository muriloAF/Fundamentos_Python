'''
Crie um programa para analisar o IMC de uma pessoa,
e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.
'''

peso = float(input('Digite sua peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura ** 2

print(f'Seu imc é: {imc}')
if imc > 40:
    print('Obesidade grau III(mórbida)')
elif imc > 39.9:
    print('Obesidade grau II(severa)')
elif imc > 34.9:
    print('Obesidade grau I')
elif imc > 29.9:
    print('Levemente acima do peso')
elif imc > 24.4:
    print('Peso ideal (parabéns)')
else:
    print('Abaixo do peso')
