'''
Escreva um programa que verifique se uma palavra é um palíndromo.
'''
'''
#Forma mais fácil:
palavra = input('Digite uma palavra: ').lower()
if palavra == palavra[::-1]
    print('É palíndromo')
else:
    print('Não é palíndromo')
'''
#Minha forma:
palavra = input('Digite uma palavra: ').lower()
x = 0
t = len(palavra)-1
for i in range(0, len(palavra[-1])+1):
    if x != t:
        j = (j.replace(palavra[x], palavra[t]))
        x += 1
        t -= 1
if j == palavra:
    print(j)
    print(palavra)
    print('É palíndromo')
    print(x)
    print(t)
else:
    print('Não é palíndromo')
    print(x)
    print(t)



