class LeastFrequentlyUsedCache:
    def __init__(self, max_size):
        self.max_size = max_size
        # Mapping of key vs frequency
        self.key_vs_freq = {}
        # Mapping of frequency vs linked-list of keys.
        self.freq_vs_keys = {}
        # The minimum frequency of any of the keys.
        self.min_freq = 1

    def get(self, key):
        if key in self.key_vs_freq:
            print(f'Key "{key}": Cache hit!')
            freq = self.key_vs_freq[key]
            self.freq_vs_keys[freq].remove(key)
            if not self.freq_vs_keys[freq]:
                print(f'Key "{key}": Deleting old linked list for frequency {freq}...')
                del self.freq_vs_keys[freq]
                if freq == self.min_freq:
                    self.min_freq += 1
            freq += 1
            self.key_vs_freq[key] = freq
            self.freq_vs_keys[freq] = self.freq_vs_keys.get(freq, [])
            self.freq_vs_keys[freq].append(key)
            print(f'Key "{key}": Frequency changed to {freq} from {freq-1}')
        else:
            print(f'Key "{key}": Cache miss!')
            if len(self.key_vs_freq) >= self.max_size:
                # Delete the oldest entry having the least frequency.
                # Delete this entry from both the maps.
                key_to_be_deleted = self.freq_vs_keys[self.min_freq][0]
                del self.key_vs_freq[key_to_be_deleted]
                del self.freq_vs_keys[self.min_freq][0]
                if not self.freq_vs_keys[self.min_freq]:
                    print(f'Key "{key}": Deleting lowest frequency list...')
                    del self.freq_vs_keys[self.min_freq]
            freq = 1
            self.min_freq = 1
            self.key_vs_freq[key] = freq
            self.freq_vs_keys[freq] = self.freq_vs_keys.get(freq, [])
            self.freq_vs_keys[freq].append(key)

    def __repr__(self):
        return f"Freq = {self.key_vs_freq}\nReverse = {self.freq_vs_keys}\n"


def main():
    cache = LeastFrequentlyUsedCache(4)
    cache.get(1)
    cache.get(2)
    cache.get(3)
    cache.get(4)
    cache.get(5)
    cache.get(2)
    cache.get(2)
    cache.get(3)
    cache.get(4)
    cache.get(5)
    print(cache)
    cache.get(1)
    print(cache)


if __name__ == "__main__":
    main()

'''
This approach has one major drawback when cache is full: a new saved item could cause the eviction of an item more frequently used than the new one. This is called cache pollution.
We can also use min-heap to implement this!
'''
