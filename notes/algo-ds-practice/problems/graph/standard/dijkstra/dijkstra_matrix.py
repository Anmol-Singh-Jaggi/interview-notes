from math import inf


def get_closest_unvisited(distances, visited):
    closest = None
    for vert, dist in distances.items():
        if vert in visited:
            continue
        if closest is None or dist < distances[closest]:
            closest = vert
    return closest


def dijkstra(matrix, src):
    # CAREFUL: Dont use heap here!
    # It will increase the complexity to O(V^2 LogV) from O(V^2).
    num_vertices = len(matrix)
    distances = {}
    for i in range(num_vertices):
        distances[i] = inf
    distances[src] = 0
    visited = set()
    for _ in range(num_vertices):
        current = get_closest_unvisited(distances, visited)
        visited.add(current)
        for neigh in range(num_vertices):
            if neigh == current:
                continue
            neigh_distance = matrix[current][neigh] + distances[current]
            if neigh_distance < distances[neigh]:
                distances[neigh] = neigh_distance
    return distances


def main():
    matrix = []
    matrix.append([0, 1, 43])
    matrix.append([1, 0, 6])
    matrix.append([43, 6, 0])
    ans = dijkstra(matrix, 2)
    print(ans)


main()
