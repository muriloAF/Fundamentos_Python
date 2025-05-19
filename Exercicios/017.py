'''
Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
'''

letra = input('Digite uma letra: ').strip()

if letra == 'a':
    print('É uma vogal')
elif letra == 'e':
    print('É uma vogal')
elif letra == 'i':
    print('É uma vogal')
elif letra == 'o':
    print('É uma vogal')
elif letra == 'u':
    print('É uma vogal')
else:
    print('É uma consoante')

#Forma alternativa:
'''Utilizamos o "in" para perguntar se a letra digitada esta contida no conjunto específico'''
print('-----------------------------------------\\-----------------------------------------')
if letra in 'aeiou':
    print('É vogal')
else:
    print('É consoante')