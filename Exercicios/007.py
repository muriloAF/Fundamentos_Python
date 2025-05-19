'''Crie um algoritmo que leia um
número e mostre o seu dobro, triplo e raiz quadrada.
'''
#Declaração de variáveis
numero = float(input('Digite um numero: '))
#Realização dos cálculos
dobro = (numero * 2)
triplo = (numero *3)
raiz = numero ** (1/2)
#Exibição dos valores
'''
print (f'O dobro é: {dobro}')
print (f'O triplo é: {triplo}')
print (f'A raiz é {raiz}')
'''

#Resolução do professor
print(f'O dobro de {numero} é {dobro}\no triplo de {numero} é {triplo}\n a raiz de {numero} é {raiz}')# O \n Siginifica quebre de linhas