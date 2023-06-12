"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Marcos'), (1, 'Maria'), (2, 'Pedro'), (3, 'Iago')]
lista = ['Marcos', 'Maria', 'Pedro']
lista.append('Iago')
# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])
    
# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')