'''
Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
'''
#Cadastro de dados
raio = float(input('Qual é o raio da esfera: '))
#Utilização das fórmulas
volume = (4/3) * 13.14 * raio ** 3
area = 4 * 13.14 * raio ** 2
#Exibição dos dados
print(f'Volume: {volume:.2f}')#":.2f significa que o python limita 2 casas após a vírgula
print(f'Area:  {area:.2f}')#":.2f significa que o python limita 2 casas após a vírgula
