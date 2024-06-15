class Node:

    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def rotate_left(self):
        if self.right is None:
            return False

        old_parent = self.parent
        self.parent = self.right
        old_right = self.right
        self.right = old_right.left

        old_right.left = self
        old_right.parent = old_parent

        if self.right is not None:
            self.right.parent = self

        if old_parent is not None:
            if old_parent.left == self:
                old_parent.left = old_right
            else:
                old_parent.right = old_right

        return True

    def rotate_right(self):
        if self.left is None:
            return False

        old_parent = self.parent
        self.parent = self.left
        old_left = self.left
        self.left = old_left.right

        old_left.right = self
        old_left.parent = old_parent

        if self.left is not None:
            self.left.parent = self

        if old_parent is not None:
            if old_parent.left == self:
                old_parent.left = old_left
            else:
                old_parent.right = old_left

        return True

    def __repr__(self):
        left = getattr(self.left, 'key', None)
        right = getattr(self.right, 'key', None)
        parent = getattr(self.parent, 'key', None)
        return f'Node <key: {self.key}, left: {left}, right: {right}, parent: {parent}>'
