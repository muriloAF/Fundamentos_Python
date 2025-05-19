'''Crie um algoritmo que leia um salário
 e simule um reajuste positivo de 60%.
'''
salario = float(input('Digite o seu salário: '))
aumento = (salario * (60/100)) + salario ;#Posso utilizar 0.6 ou 1.6(O 1.6(0.6 + 1) representa a soma do salário à propria divisão )
print(f'O salário de {salario} com o reajuste de 60% será de :{aumento}')