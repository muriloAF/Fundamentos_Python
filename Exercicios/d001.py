'''
Escreva um programa que execute o cálculo da Função
horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário
'''
#Declaração das variáveis
t = float(input('Digite o tempo em segundos: '))#É mais intuitivo criar as variáveis com nomes mais claros, como : tempo
S0= float(input('Digite o espaço inicial: '))#É mais intuitivo criar as variáveis com nomes mais claros, como: espaço zero
V0= float(input('Digite a velocidade inicial: '))#É mais intuitivo criar as variáveis com nomes mais claros, como velocidade zero
a= float(input('digite a aceleração: '))#É mais intuitivo criar as variáveis com nomes mais claros, como aceleração zero
#Utilização da fórmula
S = S0 + V0 * t + (a * (t ** 2))/2
#Exibição das respostas
print(f'A posição do objeto no tempo {t} é de {S:.2f} m')
contador =1
