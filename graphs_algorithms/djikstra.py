import heapq


def create_board(filename):
    with open(filename, "r") as file:
        board = [list(line.strip()) for line in file.readlines()]
        # powstaje lista która ma listy pól w rzędach
    return board


# zakładam że wejście na pole X to 0
def create_graph_from_board(board):
    rows = len(board)
    graph = {}
    points_x = []
    for r in range(rows):
        cols = len(board[r])
        for c in range(cols):
            node = (r, c)
            if board[r][c] == "X":
                points_x.append((r, c))
            graph[node] = {}
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < len(board[nr]):
                    neighbor = (nr, nc)
                    if board[r][c] == "J":
                        cost = 0
                    elif board[r][c] == "X":
                        cost = int(board[nr][nc]) if board[nr][nc] != "J" else 0
                    elif board[nr][nc] == "J":
                        cost = 0
                    elif board[nr][nc] == "X":
                        cost = 0
                    else:
                        cost = int(board[nr][nc])
                    graph[node][neighbor] = cost
    return graph, points_x


def print_graph(graph):
    if graph:
        for node, edges in graph.items():
            print(f"{node}:")
            for dest, weight in edges.items():
                print(f"  -> {dest} with weight {weight}")
            print()
    else:
        print("Graf jest pusty.")


filename = "graphs_algorithms/test.txt"
# filename = "graphs_algorithms/map1.txt"

board = create_board(filename)
graph, points_x = create_graph_from_board(board)


def dijkstra(graph, start, end):
    # min_distance to słownik przechowujący koszt dojscia do
    # poszczegolnych wezlow
    min_distance = {node: float("inf") for node in graph}
    min_distance[start] = 0
    # Kolejka priorytetowa dzieki niej wiemu od ktorego
    # pola dalej musimy zaczynac
    priority_queue = [(0, start)]
    # Słownik przechowujący najkrotsza sciezke do kazdego
    # wezla
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        # wybieramy pole z najmniejszym czasem by tam sie dostac i je
        # usuwamy zeby nie powtarzac
        current_distance, current_node = heapq.heappop(priority_queue)
        # kopiec min-heap, z przodu listy zawsze będzie minimalna
        # wartosc kosztu dostania sie do jakiegos noda

        # jesli heap zwroci current_node ktore jest endem to juz koniec
        if current_node == end:
            break

        # sprawdzamy kazdego sasiada danego noda
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # aktualizujemy koszt dotarcia jesli znalezlismy nizszy
            if distance < min_distance[neighbor]:
                min_distance[neighbor] = distance
                previous_nodes[neighbor] = current_node
                # do kazdego noda dodajemy poprzedniego noda z ktorego
                # przyslismy dzieki czemu pozniej mozemy odwzorowac sciezke
                heapq.heappush(priority_queue, (distance, neighbor))
                # elementy w kopcu sortowane sa wedlug distance wiec
                # jezeli dodamy do kopca nowego noda ktory bedzie najmniejszy
                # to w kolejnej iteracji on zostanie uzyty do iteracji

    # odtwarzanie najkrotszej sciezki
    path = []
    current_node = end
    while previous_nodes[current_node] is not None:
        # na poczatek listy insertowane jest current node
        # tworzymy liste od tylu
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    if path:
        path.insert(0, current_node)
    return path, min_distance[end]


start, end = points_x[0], points_x[1]
path, cost = dijkstra(graph, start, end)

print("Najkrótsza ścieżka:", path)
print("Koszt ścieżki:", cost)
