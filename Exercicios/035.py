'''
Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

A média de idade do grupo
Qual é o homem mais velho
Quantas mulheres têm menos de 20 anos
'''
mulher_vinte= 0
homem_velho = " "
media = 0.0
idade_contador = 0
for i in range(1, 5):
    nome=input('Digite seu nome: ')
    idade = int(input('Qual a sua idade: '))
    media += idade
    sx = int(input('Digite seu sexo, 1-Masculino  2-Feminino: '))
    if sx == 1:
        if idade > idade_contador:
            idade_contador = idade
            homem_velho = nome
    elif idade < 20:
        mulher_vinte +=1

print(f'{mulher_vinte} mulheres possuem mais de 20 anos')
print(f'O homem mais velho é: {homem_velho}')
print(media/4)