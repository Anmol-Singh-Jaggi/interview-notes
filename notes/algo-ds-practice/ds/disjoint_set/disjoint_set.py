class DisjointSet:
    def __init__(self) -> None:
        self.parent = {}
        self.group_size = {}

    def _add_node_if_absent(self, index: int) -> None:
        if index in self.parent:
            return
        self.parent[index] = index
        self.group_size[index] = 1

    def find_parent(self, index: int) -> int:
        # Path compression
        # Complexity = O(1) essentially
        self._add_node_if_absent(index)
        if self.parent[index] != index:
            self.parent[index] = self.find_parent(self.parent[index])
        return self.parent[index]

    def join(self, index1: int, index2: int) -> None:
        self._add_node_if_absent(index1)
        self._add_node_if_absent(index2)
        parent1 = self.find_parent(index1)
        parent2 = self.find_parent(index2)
        if parent1 == parent2:
            return
        if self.group_size[parent1] >= self.group_size[parent2]:
            parent1, parent2 = parent2, parent1
        # Union by rank
        # Complexity = O(1) essentially
        self.parent[parent1] = parent2
        # CAREFUL: Dont just increment bigger group by 1!
        self.group_size[parent2] += self.group_size[parent1]

    def get_groups(self):
        groups = {}
        for child, par in self.parent.items():
            group = groups.get(par, [])
            groups[par] = group
            group.append(child)
        return groups

    def __len__(self):
        return len(self.parent)

    def __repr__(self):
        return str(self.parent)


def main() -> None:
    disj_set = DisjointSet()
    print(disj_set.parent)
    disj_set.join(0, 1)
    print(disj_set.parent)
    disj_set.join(2, 3)
    print(disj_set.parent)
    disj_set.join(4, 5)
    print(disj_set.parent)
    disj_set.join(0, 5)
    print(disj_set.parent)
    disj_set.find_parent(5)
    print(disj_set.parent)
    print(disj_set.get_groups())


if __name__ == "__main__":
    main()
