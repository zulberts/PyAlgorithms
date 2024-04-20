from BST import BST


def test_insert_and_search():
    bst = BST()
    assert not bst.search(10)  # Szukanie w pustym drzewie
    bst.insert(10)
    assert bst.search(10)
    assert not bst.search(5)
    bst.insert(5)
    bst.insert(15)
    assert bst.search(5)
    assert bst.search(15)


def test_delete_leaf_node():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.delete(5)
    assert not bst.search(5)


def test_delete_node_with_one_child():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(12)
    bst.delete(15)
    assert not bst.search(15)
    assert bst.search(12)


def test_delete_node_with_two_children():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(12)
    bst.insert(17)
    bst.delete(15)
    assert not bst.search(15)
    assert bst.search(12)
    assert bst.search(17)


def test_delete_root_node():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.delete(10)
    assert not bst.search(10)
    assert bst.search(5)
    assert bst.search(15)


def test_delete_non_existent_node():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.delete(20)
    assert bst.search(10)
    assert bst.search(5)
    assert bst.search(15)
