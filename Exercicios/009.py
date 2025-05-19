'''
Escreva um programa que leia um tipo de dado e
usando a função type(), retorne ao usuário, qual o tipo de dado informado
'''

#O "type()" é utilizado para analisar uma variável e descobrir o tipo dela

dado = input('Digite algo: ')#Toodo o input, vem como uma string, independente do valor que for digitado
print(type(dado)) #Quando utilizamos o type, nós devemos utilizar o print para expor o tipo da variável

#Exemplos:
a = 1
b = 'Banana'

print(type(a))
print(type(b))