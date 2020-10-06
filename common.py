from classes import *
from maps import *
from noalvo import *

def find_lower_path(path_list, count_type="ordenada") -> NodePath:
    """
    Retorna o "menor" NodePath de uma lista. Pode ser baseado em:
        * Distância entre nós (ordenada)
        * Custo de cada nó (gulosa)
        * No somatório de distância e custo (A estrela)

    :param path_list: lista com todos os NodePath's da busca
    :param count_type: string contendo o tipo de comparativo de tamanho
    :return: NodePath
    """
    lower = path_list[0]

    if count_type == "ordenada":
        for path in path_list:
            if path.distance < lower.distance:
                lower = path

    elif count_type == "gulosa":
        for path in path_list:
            if path.node.cost < lower.node.cost:
                lower = path

    elif count_type == "a_estrela":
        for path in path_list:
            if (path.node.cost + path.distance) < (lower.node.cost + lower.distance):
                lower = path

    return lower




def get_another_node_from_relation(node, relation):
    if relation.node_1 == node:
        return relation.node_2
    else:
        return relation.node_1


def base_path_string(node):
    ''' Cria uma string invertida do percurso até o nó '''
    node_name = node.name

    if node.parent:
        node_name = node_name + ' > ' + base_path_string(node.parent)

    return node_name


def create_path_string(path_or_node, next_node=False):
    """
     Cria uma string do percurso realizado até o nó.

    :param path_or_node: Node ou NodePath. Realiza um tratamento diferente baseado no tipo recebido
    :param next_node: Inicialmente não recebe nada, usado apenas em chamadas recursivas
    :return:
    """

    if type(path_or_node) == NodePath:
        node_name = base_path_string(path_or_node.node)
        return node_name[::-1]

    elif type(path_or_node) == Node:
        node_name = base_path_string(path_or_node)
        node_name = node_name[::-1]

        if next_node:
            node_name = node_name + ' > ' + next_node.name

        return node_name

    else:
        return None


def reset(map):
    ''' Reseta os nós para sua versão inicial '''
    for node in map.nodes:
        map.nodes[node].status = NodeStatus.LIVRE
        map.nodes[node].parent = None

    for rel in map.relations:
        rel.status = RelationStatus.NOVA
