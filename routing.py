
# routing.py

network = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8},
    "D": {"B": 5, "C": 8, "E": 2},
    "E": {"D": 2}
}


def show_network():
    print("\nNetwork Connections:")
    for computer in network:
        print(computer, "->", network[computer])


def find_route(start, end):
    if start not in network or end not in network:
        print("Computer not found.")
        return

    distances = {}
    previous = {}
    visited = []

    for computer in network:
        distances[computer] = float("inf")

    distances[start] = 0

    while len(visited) < len(network):
        current = None
        smallest = float("inf")

        for computer in network:
            if computer not in visited and distances[computer] < smallest:
                smallest = distances[computer]
                current = computer

        if current is None:
            break

        if current == end:
            break

        visited.append(current)

        for neighbor in network[current]:
            if neighbor not in visited:
                cost = network[current][neighbor]
                new_distance = distances[current] + cost

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current

    if distances[end] == float("inf"):
        print("No route available.")
        return

    path = []
    current = end

    while current != start:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    print("Shortest route:", " -> ".join(path))
    print("Total cost:", distances[end])


def block_connection(first, second):
    if first in network and second in network[first]:
        del network[first][second]
        del network[second][first]
        print("Connection blocked successfully.")
    else:
        print("Connection does not exist.")
