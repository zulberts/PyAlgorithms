from AVL import Tree


def test_insert_and_search():
    tree = Tree()
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

    tree.insert(40)
    tree.insert(50)
    assert tree.value == 30


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


def test_deletion():
    tree = Tree()
    values_to_insert = [20, 10, 30, 5, 15, 25, 35]
    for value in values_to_insert:
        tree.insert(value)

    tree.delete(10)
    assert not tree.search(10)

    tree.delete(20)
    assert not tree.search(20)
