class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        elif node.value == key:
            return True
        elif key < node.value:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.value:
            node.left = self._delete(node.left, key)
        elif key > node.value:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temporary_value = self._min_value_node(node.right)
            node.value = temporary_value.value
            node.right = self._delete(node.right, temporary_value.value)
        return node

    def _min_value_node(self, node):
        current = node
        while (current.left is not None):
            current = current.left
        return current

    def print_tree(self):
        if not self.root:
            print("Drzewo jest puste")
            return
        levels = []
        current_level = [self.root]

        while current_level:
            levels.append(current_level)
            next_level = []
            for node in current_level:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    next_level.append(None)
                    next_level.append(None)
            if not any(next_level):
                break
            current_level = next_level

        for level, nodes in enumerate(levels):
            print(f"Poziom {level}: ", end="")
            for node in nodes:
                if node:
                    print(f"{node.value}\t", end="")
                else:
                    print("-\t", end="")
            print()
