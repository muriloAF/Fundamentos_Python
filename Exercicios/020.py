'''
Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.
'''
if int(input('Você está em boas condições de saúde? digite 1 para "sim" e 2 para "não": ')).strip() == 2:
    print('Infelizmente você não pode doar sangue')
elif int(input('Você está com todos os documento necessários? digite 1 para "sim" e 2 para "não": ')).strip() == 2:
    print('Infelizmente você não pode doar sangue')
elif float(input('Quantos kg você tem? ')) < 50:
    print('Infelizmente você não pode doar sangue')
elif int(input('Você dormiu ao menos 6 horas nas últimas 24 horas? digite 1 para "sim" e 2 para "não": ')).strip() == 2:
    print('Infelizmente você não pode doar sangue')
elif int(input('Você esta descançado e alimentado? digite 1 para "sim" e 2 para "não": ')).strip() == 2:
    print('Infelizmente você não pode doar sangue')
else:
    print('Felizmente você pode doar sangue')

#É possível fazer por aninhamento
