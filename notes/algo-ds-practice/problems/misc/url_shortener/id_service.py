class IdService():
    def __init__(self):
        self.id_counter = 0
        self.deleted_ids = set()
        pass

    def delete_id(self, id):
        assert id < self.id_counter
        self.deleted_ids.add(id)

    def _generate_new_id(self):
        new_id = self.id_counter
        self.id_counter += 1
        return new_id

    def get_next_id(self):
        next_id = None
        if not self.deleted_ids:
            next_id = self._generate_new_id()
        else:
            next_id = self.deleted_ids.pop()
        return next_id


def main():
    ids = IdService()
    id = ids.get_next_id()
    id = ids.get_next_id()
    id = ids.get_next_id()
    id = ids.get_next_id()
    print(id)
    ids.delete_id(1)
    id = ids.get_next_id()
    print(id)
    id = ids.get_next_id()
    print(id)


if __name__ == "__main__":
    main()
