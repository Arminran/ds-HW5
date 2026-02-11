import math
import random
def read_student_ids(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    ids = [line.strip() for line in lines if line.strip()]
    return ids
def student_id_to_int(sid):
    return int(sid)
M = 1000  


def hash_division(key):
    return key % M


A = (math.sqrt(5) - 1) / 2  
def hash_multiplication(key):
    frac = key * A - math.floor(key * A)
    return math.floor(M * frac)

P = 100000007  
a = random.randint(1, P-1)
b = random.randint(0, P-1)
def hash_universal(key):
    return ((a * key + b) % P) % M

class HashTableChaining:
    def __init__(self, hash_func):
        self.size = M
        self.hash_func = hash_func
        self.table = [[] for _ in range(self.size)]
        self.collisions = 0

    def insert(self, key):
        index = self.hash_func(key)
        if self.table[index]:  
            self.collisions += 1
        self.table[index].append(key)

    def get_collisions(self):
        return self.collisions

if __name__ == "__main__":
    student_ids = read_student_ids("students.txt")
    int_keys = [student_id_to_int(sid) for sid in student_ids]

    hash_funcs = [
        ("Division Method", hash_division),
        ("Multiplication Method", hash_multiplication),
        ("Universal Hashing", hash_universal)
    ]

    results = []

    for name, func in hash_funcs:
        ht = HashTableChaining(func)
        for key in int_keys:
            ht.insert(key)
        results.append((name, ht.get_collisions()))
    print("result : number colision for  student.txt (M = 1000):")
    print("-" * 50)
    for name, coll in results:
        print(f"{name}: {coll} colision")
    print("-" * 50)