from BST import BST


def main():
    tree1 = BST()
    tree2 = BST()
    tree3 = BST()

    elements1 = [15, 10, 20, 8, 12, 17, 25]
    for element in elements1:
        tree1.insert(element)

    elements2 = [30, 20, 40, 10, 25, 35, 50]
    for element in elements2:
        tree2.insert(element)

    elements3 = [5, 21, 8, 1, 3, 7, 9, 10, 11, 12, 13, 14, 15, 16]
    for element in elements3:
        tree3.insert(element)

    print("Drzewo 1:")
    tree1.print_tree()
    print("\nDrzewo 2:")
    tree2.print_tree()
    print("\nDrzewo 3:")
    tree3.print_tree()


if __name__ == "__main__":
    main()
