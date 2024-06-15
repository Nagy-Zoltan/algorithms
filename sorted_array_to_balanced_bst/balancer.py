def balance_sorted_linked_list(node, length):
    rotations = length // 2

    if node.left is not None:
        for _ in range(rotations):
            new_node = node.left
            node.rotate_right()
            node = new_node

        right_length = length // 2
        if length % 2 == 1:
            left_length = right_length
        else:
            left_length = right_length - 1

    elif node.right is not None:
        for _ in range(rotations):
            new_node = node.right
            node.rotate_left()
            node = new_node

        left_length = length // 2
        if length % 2 == 1:
            right_length = left_length
        else:
            right_length = left_length - 1

    else:
        return

    if node.left is not None:
        balance_sorted_linked_list(node.left, left_length)
    if node.right is not None:
        balance_sorted_linked_list(node.right, right_length)
