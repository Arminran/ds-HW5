def read_strings(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    strings = [line.strip() for line in lines if line.strip()]
    return strings

def ascii_sum_hash(s, M):
    total = sum(ord(ch) for ch in s)
    return total % M

def polynomial_rolling_hash(s, M, p=31):
    hash_value = 0
    power = 1
    for ch in s:
        hash_value = (hash_value + ord(ch) * power) % M
        power = (power * p) % M
    return hash_value

M = 1000

class HashTableChaining:
    def __init__(self, hash_func):
        self.size = M
        self.hash_func = hash_func
        self.table = [[] for _ in range(self.size)]
        self.collisions = 0

    def insert(self, key):
        index = self.hash_func(key, self.size)
        if self.table[index]:
            self.collisions += 1
        self.table[index].append(key)

    def get_collisions(self):
        return self.collisions

if __name__ == "__main__":
    strings = read_strings("string_dataset.txt")
    
    hash_funcs = [
        ("ASCII Sum Method", ascii_sum_hash),
        ("Polynomial Rolling Method", polynomial_rolling_hash)
    ]
    
    results = []
    
    for name, func in hash_funcs:
        ht = HashTableChaining(func)
        for s in strings:
            ht.insert(s)
        results.append((name, ht.get_collisions()))
    
    print("result : number collision for string_dataset.txt (M = 1000):")
    print("-" * 50)
    for name, coll in results:
        print(f"{name}: {coll} collision")
    print("-" * 50)