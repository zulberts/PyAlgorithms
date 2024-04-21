import random
import time
import matplotlib.pyplot as plt
from BST import BST
from AVL import Tree as AVLTree


def generate_numbers(n, max_val):
    return [random.randint(1, max_val) for _ in range(n)]


def measure_insertion(tree, numbers):
    start = time.time()
    for number in numbers:
        tree.insert(number)
    return time.time() - start


def measure_search(tree, numbers):
    start = time.time()
    for number in numbers:
        tree.search(number)
    return time.time() - start


def measure_deletion(tree, numbers):
    start = time.time()
    for number in numbers:
        tree.delete(number)
    return time.time() - start


def run_experiment(tree_class, n_values, all_numbers):
    insertion_times = []
    search_times = []
    deletion_times = []

    for n in n_values:
        # Initialize the tree based on its specific requirements
        if tree_class.__name__ == 'BST':
            tree = tree_class()
        elif tree_class.__name__ == 'Tree':
            if n == 0:
                continue
            tree = tree_class(all_numbers[0])
            numbers = all_numbers[1:n]
        else:
            print(f"Unrecognized tree class {tree_class.__name__}")
            continue

        if tree_class.__name__ == 'Tree':
            for number in numbers:
                tree.insert(number)
        else:
            for number in all_numbers[:n]:
                tree.insert(number)
        insertion_times.append(measure_insertion(tree, all_numbers[:n]))
        search_times.append(measure_search(tree, all_numbers[:n]))
        if tree_class.__name__ == 'BST':
            deletion_times.append(measure_deletion(tree, all_numbers[:n]))
        else:
            deletion_times.append(None)

    return insertion_times, search_times, deletion_times


def main():
    n_values = [1000, 2000, 5000, 10000]
    max_val = 30000
    all_numbers = generate_numbers(max_val, max_val)

    bst_insert, bst_search, bst_delete = run_experiment(BST, n_values, all_numbers)
    avl_insert, avl_search, avl_delete = run_experiment(AVLTree, n_values, all_numbers)

    plt.figure(figsize=(10, 5))
    plt.plot(n_values, bst_insert, label="BST Insertion Times")
    plt.plot(n_values, avl_insert, label="AVL Insertion Times")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.title("Insertion Performance")
    plt.legend()
    plt.savefig('trees_algorithms/tree_grphs/insertion_performance.jpg')
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(n_values, bst_search, label="BST Search Times")
    plt.plot(n_values, avl_search, label="AVL Search Times")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.title("Search Performance")
    plt.legend()
    plt.savefig('trees_algorithms/tree_grphs/search_performance.jpg')
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(n_values, bst_delete, label="BST Deletion Times")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.title("Deletion Performance (BST Only)")
    plt.legend()
    plt.savefig('trees_algorithms/tree_grphs/deletion_performance.jpg')
    plt.close()


if __name__ == "__main__":
    main()
