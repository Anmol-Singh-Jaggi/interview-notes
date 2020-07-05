class HashTable:
    '''Only supports integers as keys right now.
    Values cannot be None, obviously.
    Every operation is theoretically most efficient.
    Uses probing as collision resolution strategy.
    '''

    def __init__(self, init_size=8, load_factor_max=0.75):
        # A hash table entry will be of the form <key, value, hash, reverse_index>.
        # Hash is stored just to facilitate quicker comparison matching while finding the key.
        # That last part `reverse_index` is the index in `used_slot_indices` corresponding to this entry.
        # Start with 8 elements, because that is what happens in the official Python dict.
        self.table = [None] * init_size
        self.num_entries = 0
        self.load_factor_max = load_factor_max

        # A **contiguous** list storing the slot indices of all the used entries in the table.
        # The reason why we are maintaining this is because we want hash table iteration to be fast.
        # The hash table array itself has a lot of Dummy/None values, but this list will
        # store that info contiguously.
        # Its actual length will always be equal to the number of new entries done.
        # But when some entries are removed, it will have some `None` values at the end.
        # The number of non-None entries will always be equal to `self.num_entries`.
        # If the hash table has the data [None, 1104, None, None, 5121, None], then this array
        # will be [1, 4] indicating the 0-indexed slot indices of the keys 1104 and 5121 respectively.
        self.used_slot_indices = []
        # Do not modify this; its a constant.
        self.DUMMY_ENTRY = ()
        # IMPORTANT!! All the fields defined here should be handled in `self._copy_from_other()`.

    def __str__(self):
        ret_value = ''
        for idx, entry in enumerate(self.table):
            ret_value += '{}. {}\n'.format(idx, entry)
        return ret_value

    def size(self):
        return self.num_entries

    def get_entries(self):
        '''
        Returns the list of entries present in the hash table.
        Does not preserve the insertion order.
        '''
        entries = []
        for num_entry in range(self.num_entries):
            used_slot_index = self.used_slot_indices[num_entry]
            entry = self.table[used_slot_index]
            entries.append(entry)
        return entries

    def _compute_hash(self, key):
        return key % len(self.table)

    def _increment_probe_index(self, probe_index):
        '''
        A Linear Congruential Generator which will return all\
        values in the range `[0, len(self.table)]` exactly once.
        For proof, see `Hull–Dobell Theorem`.
        '''
        return ((5 * probe_index) + 1) % len(self.table)

    def _get_key_slot_index(self, key):
        '''
        Get the slot index in the table array where the key is present / ready-to-be-inserted.
        '''
        index = self._compute_hash(key)
        original_hash = index
        dummy_index = None
        current_probe_length = 0
        # Start probing...
        while True:
            current_probe_length += 1
            entry = self.table[index]
            if entry is None:
                # Found an empty slot, which means the key is absent.
                # Return dummy if possible, so that it will be used to insert any new entry when
                # called by `self.put()`
                return dummy_index or index
            if entry == self.DUMMY_ENTRY:
                # Save the slot index of the first dummy found.
                dummy_index = dummy_index or index
            # Comparing the hash first to avoid unnecessary key object comparisons which are costly
            elif entry[2] == original_hash and entry[0] == key:
                # Found the key!
                return index
            if current_probe_length > len(self.table):
                # Looked at all the slots, no need of proceeding further
                # This should never occur theoretically!!
                raise Exception("Hash table full!!")
            index = self._increment_probe_index(index)

    def _resize_if_needed(self):
        load_factor = (self.size() * 1.0) / len(self.table)
        if load_factor < self.load_factor_max:
            return
        # Just make a bigger hash table and copy all the entries.
        ht_bigger = HashTable(len(self.table) * 2, self.load_factor_max)
        for entry in self.get_entries():
            ht_bigger.put(entry[0], entry[1])
        self._copy_from_other(ht_bigger)

    def _copy_from_other(self, other_hash_table):
        '''
        Copy all the data from another hash table.
        '''
        self.table = other_hash_table.table
        self.num_entries = other_hash_table.num_entries
        self.load_factor_max = other_hash_table.load_factor_max
        self.used_slot_indices = other_hash_table.used_slot_indices

    def get(self, key):
        slot_index = self._get_key_slot_index(key)
        entry = self.table[slot_index]
        if entry and entry != self.DUMMY_ENTRY:
            return entry[1]
        return None

    def put(self, key, value):
        key_hash = self._compute_hash(key)
        new_entry = None
        slot_index = self._get_key_slot_index(key)
        if not self.table[slot_index]:
            # It is either None or Dummy
            # Adding a new key
            if len(self.used_slot_indices) == self.num_entries:
                # Expand the used_slot_indices list
                self.used_slot_indices.append([])
            # A new reverse-index value will always go at the end
            reverse_index = self.num_entries
            new_entry = (key, value, key_hash, reverse_index)
            self.used_slot_indices[reverse_index] = slot_index
            self.num_entries += 1
        else:
            # An entry is already present for the key. So overwrite...
            # Just change the value part. Rest of the tuple is same as the entry being overwritten.
            new_entry = (key, value, key_hash, self.table[slot_index][3])
        self.table[slot_index] = new_entry
        self._resize_if_needed()
        return value

    def _remove_from_used_slot_indices(self, entry):
        '''
        Removes the reverse index of the entry.
        It just copies the last non-None value in `used_slot_indices` to the reverse index,
        thus maintaining the contiguous property.
        '''
        # The index of this entry in `used_slot_indices`
        reverse_index = entry[3]
        if reverse_index == self.num_entries - 1:
            # If this is already the reverse index, then just make it None and return.
            self.used_slot_indices[reverse_index] = None
            return
        # Bring the last non-None value present in `used_slot_indices` to this place.
        self.used_slot_indices[reverse_index] = self.used_slot_indices[
            self.num_entries - 1]
        # Update the `reverse_index` part of the entry pointed to by the last
        # non-None value.
        # The slot index of the entry described above.
        slot_index = self.used_slot_indices[reverse_index]
        entry = self.table[slot_index]
        self.table[slot_index] = (entry[0], entry[1], entry[2], reverse_index)
        # Mark the last reverse index position as empty.
        self.used_slot_indices[self.num_entries - 1] = None

    def remove(self, key):
        slot_index = self._get_key_slot_index(key)
        if not self.table[slot_index]:
            raise KeyError('Key "{}" not found'.format(key))
        entry = self.table[slot_index]
        self.table[slot_index] = self.DUMMY_ENTRY
        self._remove_from_used_slot_indices(entry)
        self.num_entries -= 1


def main():
    ht = HashTable()
    ht.put(1, 2)
    ht.put(9, 3)
    ht.put(17, 5)
    ht.remove(9)
    print(ht.get(17))
    ht.put(7, 10)
    ht.put(0, 11)
    ht.put(8, 10)
    ht.put(10, 10)
    ht.remove(17)
    ht.put(1, 3)
    ht.put(11, 12)
    ht.put(100, 3)
    ht.put(201, 12)
    ht.put(200, 12)
    print(ht.get_entries())


if __name__ == "__main__":
    main()
