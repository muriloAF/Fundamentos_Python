'''
#Operações Matemáticas
print(1 + 1)
print(8000 - 100)
print(10 % 2)
print(5 * 5)
print( 10 / 2)
#Variáveis
x = 5
y = 2
xy = x+y
print ("A soma de x e y é:", xy)

#Retorno de informações com variáveis
idade=56
print(f"a sua idade é {idade}")

#Leitura de Informações
x= input('Digite algo: ')
print(f'Seu nome é {x}')

#Leitura de Informações Numéricas
x = int(input('Digite um numero: '))
print(f'O dobro de x é{x * 2}')
'''
# Strings:
'''Uma string é representada como um vetor, que se inicia por 0'''
nome = 'Murilo Alves da Fonseca'
# Formatações:
'''Existem formas de formatar uma string e um número, como:'''
# {media:.2f}. O ":.2f" delimita duas casas decimais após a vírgula
# Existem também o f string, permite a exibição de variáveis utilizando apenas "{VARIÁVEL}"


# Fatiamento de strings
print(nome[0])
print(nome[3:14])
print(nome[:7])  # O ESPAÇO VAZIO REPRESENTA 0
print(nome[8:])  # O ESPAÇO VAZIO REPRESENTA 0

# Análise
print(len(nome))  # CONTA A QUANTIDADE DE CARACTERES INCLUINDO OS ESPAÇOS
print(nome.count('l'))  # CONTA QUANTOS 'l'(MÍNUSCULOS TEM) NO NOME
print(nome.find('i'))  # ENCONTRA A LETRA 'i', PRESENTE NO NOME.
print(nome.rfind('i'))  # ENCONTRA A LETRA 'i', PRESENTE NO NOME. ESTE ENCONTRA O ULTIMPO EM ESPECIAL

# Transformação
print(
    nome.upper())  # DEIXA TODAS AS LETRAS EM MAIÚSCULO. É APENAS PARA O OUTPUT, ELA NÃO FICA MAIÚSCULA DEFINITIVAMENTE
# nome = nome.upper(). ISSO ATRIBUI UM NOVO VALOR A VARIÁVEL NOME, DEXIANDO ELA MAIÚSCULA DEFINITIVAMENTE
print(nome.lower())  # ISSO DEIXA A STRING EM LETRAS MINÚSCULAS
print(nome.replace('M', 'A'))  # TEM A FUNÇÃO DE TROCAR AS LETRAS DE LUGAR, OU SEJA: "Aurilo Muves da Fonseca"
print(
    nome.split())  # O SPLIT DIVIDE A STRING E ALOCA CADA PALAVRA EM UMA VETOR, EXEMPLO: [Murilo, Alves, da, Fonseca]:0 1, 2, 3
nome = input(
    'Nome: ').strip()  # O STRIP RETIRA TODOS OS ESPAÇOS DA DIREITA E DA ESQUERDA DA STRING, DEIXANDO ELA MAIS LIMPA. PORÉM ELE NÃO RETIRA OS ESPAÇOS CENTRAIS
print(nome)
#Condicionais
altura = 3
if altura > 2:
    print("Não pode andar no brinquedo")
else:
    print("Pode andar")

altura = 5
if altura > 2:
    print('Você não pode entrar')
elif altura < 1:
    print('Nem pensar')
else:
    print('Você pode andar no brinquedo')

#Bibliotecas
'''No Python existem bibliotecas que podem ser usadas para executar algumas ações em específico, 
como a de escolher um número aleatório:'''
#Importação da Biblioteca radom (usada para gerar valores aleatórios)
import random
import time
#Uso da função randint (Gera um número aleatório inteiro entre 1 e 3)
aleatorio = random.randint(1, 3)

#Retorno da variável aleatório gerada
print(aleatorio)

#REPETIÇÕES
for i in range (1, 10):
    print('*')
for i in range (1, 100):
    print(i)
for i in range(100, 1, -1):
    print(i)

soma = 0
for i in range(0, 5):
    n = int(input('Numero: '))
    soma += n
print (soma)