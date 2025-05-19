'''
Escreva um programa que peça ao usuário uma senha e verifique se ela está correta (a senha correta é "python123").
'''

senha = input('Digite a senha para entrar: ')

if senha != 'python123':
    print('A senha está incorreta, tente novamente.')
else:
    print('A senha está correta, bem vindo!')