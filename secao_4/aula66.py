"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Definição da função: refere-se à função RECEBENDO PARÂMETROS NA SUA DEFINIÇÃO. Quando se passa os VALORES, aí dizemos que estamos passando os ARGUMENTOS DA FUNÇÃO.
def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3) # ARGUMENTO POSICIONAL
soma(1, y=2, z=5)

print(1, 2, 3, sep='-') 