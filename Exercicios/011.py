'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao to-do (sem considerar os espaços)
Quantas letras tem o primeiro nome
'''
nome = input('Digite seu nome completo: ').strip()
print(f'Seu nome com todas as letras em maiúsculas fica: {nome.upper()}'
      f'\nSeu nome com todas as letras em minúsculas fica: {nome.lower()}'
      f'\nO seu nome possui: ', len(nome) - nome.count(' '),' letras')  # Somei tudo e depois subtrai pelos espaço, para descobrir a quantidade de caracteres

nome = nome.split()
print('Qauntidade de letras do primeiro nome', len(nome[0]))
