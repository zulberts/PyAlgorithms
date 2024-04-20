import random
import time
import matplotlib.pyplot as plt
from AVL import Tree as AVLTree


def generate_data(size, upper_limit):
    return [random.randint(1, upper_limit) for _ in range(size)]


def test_avl_operations(data, steps):
    insert_times = []
    search_times = []

    for n in steps:
        subset = data[:n]
        avl = AVLTree()

        # Test insertion
        start_time = time.time()
        for value in subset:
            avl.insert(value)
        insert_times.append(time.time() - start_time)

        # Test search
        start_time = time.time()
        for value in subset:
            avl.search(value)
        search_times.append(time.time() - start_time)

    return insert_times, search_times


def main():
    data_size = 10000
    steps = list(range(1000, 10001, 1000))
    data = generate_data(data_size, 30000)
    insert_times, search_times = test_avl_operations(data, steps)

    plt.figure(figsize=(10, 5))
    plt.plot(steps, insert_times, label="Insertion Times", marker="o")
    plt.title("AVL Insertion Time")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.savefig("avl_insertion_time.jpg")
    plt.clf()

    plt.figure(figsize=(10, 5))
    plt.plot(steps, search_times, label="Search Times", marker="o")
    plt.title("AVL Search Time")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.savefig("avl_search_time.jpg")


if __name__ == "__main__":
    main()
