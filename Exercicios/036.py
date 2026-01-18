'''
Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
'''
b = 0
a = 0
peso_maior = 0
peso_menor = 0
nome = input('Digite o seu nome: ')
for i in range(1, 8):
    peso = float(input('Digite seu peso: '))
    if i == 1:
            peso_maior = peso
    if i >= 2:
        if peso_menor < peso:
            peso_menor = peso
    if peso_maior < peso_menor:
        a = peso_menor
        b = peso_maior
        peso_maior = a
        peso_menor = b
'''        
#Livros interessantes
        ideias que colam
        okyakusama
        manual de processamento de dados Favero
        ortodoxia
        introdução a vida intelectual
#Dramas
        memórias do subsoslo
        crime e castigo
        conifssões santo Agostinho
        irmãos karamaóv
'''





print(f'Peso menor: {peso_maior}')
print(f'Peso maior: {peso_menor}')
