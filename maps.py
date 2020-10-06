from classes import *

def no_alvo():
    a = input('Nó alvo: ')
    return a

a = no_alvo()

def create_map_by_dict(_dict) -> Map:
    if 'type' in _dict:

        # Teste de Criação de Mapa para buscas não-ordenadas
        if _dict['type'] == SearchTypes.NAO_ORDENADA:

            # Valida se os campos do dicionário existem.
            if 'nodes' in _dict and 'adjacent' in _dict and 'first' in _dict and 'last' in _dict:
                return create_map_type_0(_dict)

            else:
                print('Não foi possível criar o mapa pois falta algum campo.')

        elif _dict['type'] == SearchTypes.ORDENADA:

            # Valida se os campos do dicionário existem.
            if 'nodes' in _dict and 'relations' in _dict and 'first' in _dict and 'last' in _dict:
                return create_map_type_1(_dict)

            else:
                print('Não foi possível criar o mapa pois falta algum campo.')

    return None


def create_map_type_0(_dict) -> Map:
    """
    Cria um mapa para buscas não ordenadas (Largura, Profundidade e Backtracking)

    :param _dict: Dicionário contendo as informações sobre o mapa
    :return: Map
    """
    new_map = Map()
    new_map.name = _dict['map_name']
    new_map.type = _dict['type']

    try:
        # Cria os nós
        for node in _dict['nodes']:
            new_map.nodes[ node['name'] ] = Node( node['name'] )

        # Cria as Adjacencias
        for adj in _dict['adjacent']:
            for key, value in adj.items():
                if key in new_map.nodes:
                    for n in value:
                        if n in new_map.nodes:
                            new_map.nodes[key].adjacent_node.append(new_map.nodes[n])
                else:
                    # print("ERRO")
                    raise Exception("Erro no dicionário do mapa. Esse nó da relação não existe no mapa!")

        new_map.start_node = new_map.nodes[_dict['first']]
        new_map.end_node = new_map.nodes[_dict['last']]

    except Exception as exc:
        return None

    return new_map


map_dicts = [
    {
        "map_name": "Mapa para buscas não ordenadas",
        "type": SearchTypes.NAO_ORDENADA,
        "nodes": [
            { "name": "A" },
            { "name": "B" },
            { "name": "C" },
            { "name": "D" },
            { "name": "E" },
            { "name": "F" },
            { "name": "G" },
            { "name": "H" },
            { "name": "I" },
            { "name": "J" },
            { "name": "L" },
            { "name": "M" },
            { "name": "N" },
            { "name": "O" },
            { "name": "P" },
            { "name": "Q" },
            { "name": "R" },
            { "name": "S" },
        ],
        "adjacent": [
            # Tem que seguir a ordem Baixo, Esquerda, Direita, Cima.
            # Colocar aspas vazias caso não possua relação de adjacencia (apenas por uma questão de organização)
            { "A" : [ "B", "", "", "E" ] },
            { "B" : [ "C", "", "A", "F" ] },
            { "C" : [ "", "", "B", "" ] },
            { "D" : [ "", "", "", "H" ] },
            { "E" : [ "", "A", "", "I" ] },
            { "F" : [ "G", "B", "", "" ] },
            { "G" : [ "H", "", "F", "L" ] },
            { "H" : [ "", "D", "G", "" ] },
            { "I" : [ "J", "E", "", "N" ] },
            { "J" : [ "", "", "I", "O" ] },
            { "L" : [ "M", "G", "", "" ] },
            { "M" : [ "", "", "L", "Q" ] },
            { "N" : [ "", "I", "", "" ] },
            { "O" : [ "P", "J", "", "R" ] },
            { "P" : [ "Q", "", "O", "S" ] },
            { "Q" : [ "", "M", "P", "" ] },
            { "R" : [ "", "O", "", "" ] },
            { "S" : [ "", "P", "", "" ] },
        ],
        "first": "A",
        "last": a,
    }
]

a = ''

