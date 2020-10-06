from typing import List
from enum import Enum

class NodeStatus(Enum):
    ''' Utilizado nas Buscas em Largura, Profundidade e Backtracking '''
    LIVRE = 0
    ABERTO = 1
    VISITADO = 2
    FECHADO = 3


class RelationStatus(Enum):
    ''' Utilizado nas Buscas Ordenadas e Informadas'''
    NOVA = 0
    ABERTO = 1
    EXPLORADO = 2


class SearchTypes(Enum):
    """ Enum utilizada nos dicionários de mapas para definir para qual tipo de busca o mapa se identifica """
    NAO_ORDENADA = 0
    ORDENADA = 1


class Node(object):
    ''' Indica um nó no percurso e seus atributos '''

    def __init__(self, name, cost=0):
        self.name = name.upper()
        self.relations: List[NodeRelation] = []
        self.adjacent_node: List[Node] = []
        self.status = NodeStatus.LIVRE
        self.parent = None
        self.cost = cost

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def add_adjacent_node(self, node):
        self.adjacent_node.append(node)


class NodeRelation(object):
    ''' Indica a relação entre dois nós e sua distância e custo. '''

    def __init__(self, node1, node2, distance):
        self.node_1 = node1
        self.node_2 = node2
        self.distance = distance
        self.status = RelationStatus.NOVA

        node1.relations.append(self)
        node2.relations.append(self)


class NodePath(object):
    ''' Cria um caminho de um nó até outro, cuja soma total da distância é baseada em caminhos anteriores '''

    node = None
    parent_node = None
    distance = 0

    def __init__(self, node, parent_node, prev_path, path_list, relation_list):
        '''
            node: Node                            - Indica o nó final deste caminho. \n
            parent_node: Node                     - Indica o nó que antecede este caminho. \n
            prev_path: NodePath                   - Indica o percurso até aquele nó. \n
            path_list: List[ NodePath ]           - Recebe uma lista de todos os NodePath já traçados. \n
            relation_list: List[ NodeRelation ]   - Recebe uma lista de todas as relações entre nós.
        '''

        self.node = node

        # Se possuir um nó pai (nó raiz)
        if parent_node:
            self.parent_node = parent_node

            # Busca a NodeRelation dos nós
            rel = find_relation(node, parent_node, relation_list)

            # Define a própria distância do Path baseado na distância do path anterior
            if prev_path and rel:
                self.distance = prev_path.distance + rel.distance
                rel.status = RelationStatus.EXPLORADO

        # Se não possuir, significa que a distância é 0 pois é o nó raiz ;)
        else:
            self.distance = 0


    def adjust_best_path(self, path_list, search_type="ordenada"):
        """
        Chamada ao criar um novo NodePath().
        Busca todos os NodePath que terminam no mesmo lugar e remove aqueles de maior distância total

        :param path_list:
        :param search_type:
        :return:
        """

        # Define o parente do nó
        self.node.parent = self.parent_node

        # Checa todos os caminhos dentro da path list para avaliar se existe algum caminho que resulta no mesmo nó
        for path in path_list:

            # Se os nós finais coincidirem, remove o caminho com maior distância
            if path.node == self.node and path != self:

                # Define o menor caminho baseado na distância
                if search_type == "ordenada":

                    # Dá preferência por manter os caminhos antigos. Não faz diferença de qualquer forma.
                    if self.distance >= path.distance:

                        # Reajusta o parente do nó para o anterior.
                        self.node.parent = path.parent_node
                        print('  *** Este novo caminho ( Dist.:', self.distance,
                              ') é maior ou igual ao anterior ( Dist.:', path.distance,
                              '), portanto será desconsiderado.')
                        path_list.remove(self)

                    else:
                        print('  *** Este novo caminho até', self.node,
                              'é mais curto! ( Distância Total: ', self.distance,')')
                        path_list.remove(path)

                # Define o menor caminho baseado no custo
                elif search_type == "gulosa":

                    # Dá preferência por manter os caminhos antigos. Não faz diferença de qualquer forma.
                    if self.node.cost >= path.node.cost:
                        # Reajusta o parente do nó para o anterior.
                        self.node.parent = path.parent_node
                        path_list.remove(self)

                    else:
                        path_list.remove(path)

                # Define o menor caminho baseado na distância E no custo (somatório)
                else:

                    # Dá preferência por manter os caminhos antigos. Não faz diferença de qualquer forma.
                    if (self.distance + self.node.cost) >= (path.distance + path.node.cost):

                        # Reajusta o parente do nó para o anterior.
                        self.node.parent = path.parent_node
                        print('  *** Este novo caminho ( Dist. + Custo:', str(self.distance + self.node.cost),
                              ') é maior ou igual ao anterior ( Dist. + Custo:', str(path.distance + path.node.cost),
                              '), portanto será desconsiderado.')
                        path_list.remove(self)

                    else:
                        print('  *** Este novo caminho até', self.node,
                              'é mais curto! ( Dist. + Custo:', str(self.distance + self.node.cost),')')
                        path_list.remove(path)



def find_relation(node1, node2, relation_list):
    ''' Encontra uma relação entre dois nós dentro de uma lista de NodeRelation '''

    for rel in relation_list:

        if node1.name == rel.node_1.name and node2.name == rel.node_2.name:
            return rel

        elif node2.name == rel.node_1.name and node1.name == rel.node_2.name:
            return rel

    return False


class Map(object):
    ''' Funciona como uma lista que guarda todos os nós e suas relações'''

    def __init__(self, name='Mapa', type=SearchTypes.NAO_ORDENADA):
        self.name = name
        self.type = type
        self.nodes = {}
        self.relations = []
        self.start_node = None
        self.end_node = None





