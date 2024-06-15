from balancer import balance_sorted_linked_list
from node import Node

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

root = Node(L[0])
nodes = [root]

node = root
for elem in L[1:]:
    new_node = Node(elem, parent=node)
    node.right = new_node
    node = new_node
    nodes.append(node)


print('\nBefore balancing:')
for node in nodes:
    print(node)

balance_sorted_linked_list(nodes[0], len(nodes))

print('\nAfter balancing:')
for node in nodes:
    print(node)
