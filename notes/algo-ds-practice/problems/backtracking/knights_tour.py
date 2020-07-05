def get_neighbours(board_dimensions, pos):
    rows, cols = board_dimensions
    neighbours = []
    posx, posy = pos
    # 4 straight
    neighbours.append((posx - 3, posy))
    neighbours.append((posx, posy + 3))
    neighbours.append((posx + 3, posy))
    neighbours.append((posx, posy - 3))
    # 4 diagonal
    neighbours.append((posx - 2, posy + 2))
    neighbours.append((posx + 2, posy + 2))
    neighbours.append((posx + 2, posy - 2))
    neighbours.append((posx - 2, posy - 2))
    valid_neighbours = []
    for neigh in neighbours:
        x, y = neigh
        if x >= 0 and y >= 0 and x < rows and y < cols:
            valid_neighbours.append((x, y))
    return valid_neighbours


def find_tour(board_dimensions, pos, visited, tour):
    visited.add(pos)
    tour.append(pos)
    if len(tour) == board_dimensions[0] * board_dimensions[1]:
        return True
    for neigh in get_neighbours(board_dimensions, pos):
        if neigh not in visited:
            is_tour_found = find_tour(board_dimensions, neigh, visited, tour)
            if is_tour_found:
                return True
    visited.remove(pos)
    tour.pop()
    return False


def find_any_tour(board_dimensions):
    rows, cols = board_dimensions
    for i in range(rows):
        for j in range(cols):
            tour = []
            print((i, j))
            is_tour_found = find_tour(board_dimensions, (i, j), set(), tour)
            if is_tour_found:
                return tour
    return None


def main():
    board_dimensions = (10, 10)
    tour = []
    find_tour(board_dimensions, (0, 0), set(), tour)
    # tour = find_any_tour(board_dimensions)
    print(tour)


main()
