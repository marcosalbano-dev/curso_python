nome = 'Marcos Albano'
altura = 1.69
peso = 92
imc = peso / (altura ** 2)
# f --> fstrings
linha_1 = f'{nome} tem {altura:.2f} de altura' 
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)
# print(nome, 'tem', altura, 'de altura,')
# print('pesa', peso, 'quilos e seu imc é')
# print(imc)