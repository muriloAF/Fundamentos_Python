'''
Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “a”
Em que posição ela aparece a primeira vez
Em que posição ela aparece na última vez
'''

frase = input('Escreva uma frase motivadora: ').strip().lower()  # Utilizo o lower para deixar todas as letras em minúsculo, inclusive o "a"
print(f'A quantidade de vezes que "a" letra a aparece é: {frase.count("a")}'
      f'\n A primeira veze que "a" letra a aparece é na posição: {frase.find("a") + 1}'  # Utilizo o +1, pois o find começa a contar peço 0
      f'\n A quantidade de vezes que a letra "a" aparece é: {frase.rfind("a") + 1}')  # O "rfind" exibe o último valor, já o "find" exibe o primeiro. Utilizo o +1, pois o find começa a contar peço 0
