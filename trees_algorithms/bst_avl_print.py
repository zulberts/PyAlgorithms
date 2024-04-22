from BST import BST
from AVL import Tree


def main():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(12)
    bst.insert(17)
    bst.delete(15)
    bst.insert(1)
    bst.insert(16)
    bst.insert(2)
    bst.insert(11)
    bst.insert(12)
    bst.print_tree()
    avl = Tree()
    avl.insert(1)
    avl.insert(2)
    avl.insert(10)
    avl.insert(11)
    avl.insert(14)
    avl.insert(1)
    avl.insert(12)
    avl.insert(9)
    avl.print_tree()


if __name__ == "__main__":
    main()
