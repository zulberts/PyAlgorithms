class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def insert(self, number):
        if self.value is None:
            self.value = number

        if number >= self.value:
            if self.right is None:
                self.right = Tree(number)
            else:
                self.right.insert(number)

        if number < self.value:
            if self.left is None:
                self.left = Tree(number)
            else:
                self.left.insert(number)

        if self.height_difference() > 1 and number > self.right.value:
            print("left")
            self.LeftRotate()
        if self.height_difference() > 1 and number < self.right.value:
            print("rightleft")
            self.right.RightRotate()
            self.LeftRotate()
        if self.height_difference() < -1 and number > self.left.value:
            print("leftright")
            self.left.LeftRotate()
            self.RightRotate()
        if self.height_difference() < -1 and number < self.left.value:
            print("right")
            self.RightRotate()

        self.height = 1 + max(self.left_height(), self.right_height())

    def LeftRotate(self):
        second = self.right
        third = second.left

        self.right = third
        second.left = self.tree()

        second.left.height = 1 + max(second.left.left_height(),
                                     second.left.right_height())
        second.height = 1 + max(second.left_height(),
                                second.right_height())
        self.setTree(second)

    def RightRotate(self):
        second = self.left
        third = second.right

        self.left = third
        second.right = self.tree()

        second.right.height = 1 + max(second.right.left_height(),
                                      second.right.right_height())
        second.height = 1 + max(second.left_height(),
                                second.right_height())
        self.setTree(second)

    def left_value(self):
        if self.left is None:
            return None
        return self.left.value

    def right_value(self):
        if self.right is None:
            return None
        return self.right.value

    def left_height(self):
        if self.left is None:
            return 0
        return self.left.height

    def right_height(self):
        if self.right is None:
            return 0
        return self.right.height

    def height_difference(self):
        left = self.left.height if self.left else 0
        right = self.right.height if self.right else 0
        return right-left

    def tree(self):
        tree = Tree(self.value)
        tree.left = self.left
        tree.right = self.right
        tree.height = self.height
        return tree

    def setTree(self, tree: "Tree"):
        self.value = tree.value
        self.left = tree.left
        self.right = tree.right
        self.height = tree.height

    def search(self, number):
        if self.value == number:
            return True
        if self.right is not None and number > self.value:
            return self.right.search(number)
        if self.left is not None and number < self.value:
            return self.left.search(number)
        return False

    def print_tree(self):
        lista = [self]
        new_list = []
        while True:
            value_list = []
            for tree in lista:
                value_list.append(tree.value if tree is not None else None)
                new_list.append(tree.left if tree is not None else None)
                new_list.append(tree.right if tree is not None else None)
            print(value_list)
            if all([t is None for t in new_list]):
                break

            lista = new_list
            new_list = []


tree = Tree(2)
print(tree.value)
print(tree.left_value(), " ", tree.right_value())
tree.insert(3)
tree.insert(5)
tree.insert(4)

print(tree.value)
print(tree.left_value(), " ", tree.right_value())
print(tree.height_difference())
print(tree.height, tree.left.height, tree.right.height)
print(tree.search(0))
tree.print_tree()
