"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# entrada = input('Digite um número inteiro: ')

# try:
#     numero_int = int(entrada)
#     mod = numero_int % 2
#     if mod == 0:
#         print(f'O número é par: {numero_int}')
#     else:
#         print('O número é ímpar')
# except:
#      print('Isso não é um número inteiro')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Isso não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('Digite a hora em números interos: ')

# try:
#     hora = int(entrada)
#     bom_dia = hora >= 0 and hora <= 11
#     bom_tarde = hora >= 12 and hora <= 17
#     bom_noite = hora >= 18 and hora <= 23
       
#     if bom_dia:
#         print('Olá, bom dia!')
#     elif bom_tarde:
#         print('Olá, bom tarde!')
#     elif bom_noite:
#         print('Olá, boa noite!')
#     else:
#         print('Isso não é uma hora válida')
# except:
#      print('Por favor, digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')

try:
    if nome.isdigit():
        print('Isso é um número')
    else:
        nome_tamanho = len(nome) 
        nome_curto = nome_tamanho <= 4
        nome_normal = nome_tamanho >= 5 and nome_tamanho <= 6
        nome_grande = nome_tamanho >=6
        if nome_curto:
            print('Seu nome é de tamanho curto') 
        elif nome_normal:
            print('Seu nome é de tamanho normal') 
        elif nome_grande:
            print('Seu nome é de tamanho grande') 
except:
    print('Isso não é um nome')
