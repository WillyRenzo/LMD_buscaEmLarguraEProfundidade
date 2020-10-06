from maps import *

from buscas.busca_largura      import printa_busca_em_largura
from buscas.busca_profundidade import printa_busca_em_profundidade

map_list = []
for _dict in map_dicts:
    map_list.append( create_map_by_dict(_dict) )

while True:

    print('\n ~~~~~~~~~~ Ações ~~~~~~~~~~ \n')
    
    print('1. Realizar Busca em Largura')
    print('2. Realizar Busca em Profundidade')

    print('\n0. Sair \n')

    user_input = input('Selecione: ')
    print('\n')


    if   user_input == 1 or user_input == '1':
        printa_busca_em_largura(map_list)

    elif user_input == 2 or user_input == '2':
        printa_busca_em_profundidade(map_list)

    elif user_input == 0 or user_input == '0' or user_input == 'exit':
        print('\n- Okay! Saindo...')
        break
