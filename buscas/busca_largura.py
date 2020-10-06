from common import *

def busca_em_largura(map):
    """
    Realiza uma Busca em Largura, retornando se encontrou o nó,
    qual o caminho realizado e qual o caminho encontrado até o nó.

    :param map: Mapa contendo os nós, o nó final e nó inicial
    :return:
    """

    success = False
    visiting_node_path = ''
    final_node_path = ''

    queue = []
    queue.append(map.start_node)

    while len(queue):
        node = queue[0]
        node.status = NodeStatus.VISITADO
        visiting_node_path = visiting_node_path + node.name + ' > '

        # Se for o último nó
        if node == map.end_node:
            success = True
            final_node_path = create_path_string(node)

        else:
            if not success:
                print('\n * Verificando nó', node.name, 'buscando nós adjacentes não visitados')

                # Para cada nó adjacente, faça...
                for adjacent in node.adjacent_node:

                    # Se o nó adjacente estiver a abrir
                    if adjacent.status == NodeStatus.LIVRE:
                        print(' ** Nó', adjacent.name, 'encontrado!')

                        # Define o nó atual como raíz do nó adjacente
                        adjacent.status = NodeStatus.ABERTO
                        adjacent.parent = node
                        queue.append(adjacent)

        # Remove o primeiro elemento da fila
        node.status = NodeStatus.FECHADO
        queue.pop(0)
        if not success:
            print(' *** Nó', node.name, 'verificado.')

    # Remove o último ' > ' da string
    visiting_node_path = visiting_node_path[:-3]

    # Reseta as alterações nos nós do mapa
    reset(map)

    return {
        'success': success,
        'visiting_node_path': visiting_node_path,
        'final_node_path': final_node_path
    }



def printa_busca_em_largura(map_list):
    for map in map_list:
        if map.type == SearchTypes.NAO_ORDENADA:

            print('- Realizando Busca em Largura em:', map.name, '\n')
            return_dict = busca_em_largura(map)

            if return_dict['success']:
                print('\n- O nó', map.end_node.name, 'foi encontrado!\n'
                      '- Caminho percorrido:', return_dict['visiting_node_path'],'\n'
                      '- Caminho até o nó:', return_dict['final_node_path']
                     )

            else:
                print('- O nó não pôde ser encontrado! :(')

