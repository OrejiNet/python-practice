# Búsqueda de amplitud 
# vertex = vertice o nodo
# edge   = arista que conecta 2 nodos

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = [] # neighboors
        self.visited = False


def breadth_first_search(start_node):

    # FIFO: First item we insert will be the first one to take out
    queue = [start_node]
    actual_node = True

    # we keep looping until de queue becomes empty
    while queue:

        # remove and return the first item we have inserted into the list
        actual_node = queue.pop(0)
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            if not n.visited:
                n.visited = True
                queue.append(n)


if __name__ == '__main__':

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)


    breadth_first_search(node1)



#application

# garbage collector
# serialization
# discover surrouding

# What is the running time complexity of breadth-first search?
# O(V+E)


# What is the main problem with breadth-first search?
# It is too slow for graph traversing 