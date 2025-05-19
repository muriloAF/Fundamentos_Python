'''
Crie um programa que leia um nome, e mostre o primeiro e o último nome
'''

nome = input('Digite seu nome completo: ').split().strip()
ultimo_nome = len(nome) - 1  # O "-1" é utilizado pois a lista inicia a contagem por 0, mas o len inicia por 1. Ou seja, em um index que vá de 0 até 4 o len contaria 5, porém queremos o valor do ultimo, que seria 4, portanto 4-1=4
print(f'O seu primeiro nome é {nome[0]}'  # Exibição
      f'\n O seu último nome é:  {nome[ultimo_nome]}')  # Exibição
