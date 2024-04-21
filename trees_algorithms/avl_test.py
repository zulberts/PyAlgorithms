from AVL import Tree


def test_insert_and_search():
    tree = Tree()
    assert not tree.search(5)
    values_to_insert = [20, 10, 30, 5, 15, 25, 35]
    for value in values_to_insert:
        tree.insert(value)

    for value in values_to_insert:
        assert tree.search(value)

    assert not tree.search(100)


def test_rotations():
    tree = Tree()
    tree.insert(30)
    tree.insert(20)
    tree.insert(10)
    assert tree.value == 20

    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    assert tree.value == 10
    assert tree.left.value == 5
    assert tree.right.value == 20
    assert tree.left.left.value == 3
    assert tree.left.right is None
    assert tree.right.left.value == 15
    assert tree.right.right.value == 30


def test_height_balance():
    tree = Tree()
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(10)
    tree.insert(25)
    tree.insert(35)
    tree.insert(50)

    assert tree.height == 3
    assert tree.height_difference() in [-1, 0, 1]


def test_height():
    tree = Tree()
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(10)
    tree.insert(25)
    assert tree.height == 3
    assert tree.right.height == 1
    assert tree.left.height == 2
    assert tree.left.left.height == 1
    assert tree.left.right.height == 1
