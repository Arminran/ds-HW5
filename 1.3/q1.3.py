import os
import sys
from typing import Optional

class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.table = [None] * size
        self.probe_count = 0
        self.insert_count = 0
    
    def primary_hash(self, key: str) -> int:
        return sum(ord(c) for c in key) % self.size
    
    def polynomial_hash(self, key: str, p: int = 31) -> int:
        hash_val = 0        
        power = 1
        for c in key:
            hash_val = hash_val + (ord(c) - ord('a') + 1) * power
            power = power * p
        return hash_val
    
    def secondary_hash(self, key: str) -> int:
        hash_val = self.polynomial_hash(key, p=31)
        X = 997  
        step = X - (hash_val % X)
        return step if step != 0 else 1
    
    def linear_probing(self, key: str, value: int = 1) -> int:
        hash_index = self.primary_hash(key)
        probes = 1  
        
        while self.table[hash_index] is not None:
            probes += 1
            hash_index = (hash_index + 1) % self.size
            if probes > self.size:  
                break
        
        self.table[hash_index] = (key, value)
        return probes  
    
    def quadratic_probing(self, key: str, value: int = 1) -> int:    
        base_index = self.primary_hash(key)
        probes = 1  
        i = 1
        
        while self.table[base_index] is not None:
            probes += 1
            base_index = (self.primary_hash(key) + i * i) % self.size
            i += 1
            if probes > self.size: 
                break
        
        self.table[base_index] = (key, value)
        return probes  
    
    def double_hashing(self, key: str, value: int = 1) -> int:
        hash_index = self.primary_hash(key)
        step = self.secondary_hash(key)
        probes = 1  
        
        while self.table[hash_index] is not None:
            probes += 1
            hash_index = (hash_index + step) % self.size
            if probes > self.size:  
                break
        
        self.table[hash_index] = (key, value)
        return probes  


def read_dataset(filename: str) -> list:
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found!")
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    strings = [line.strip() for line in lines if line.strip()]
    return strings


def compare_collision_methods(dataset: list, table_size: int = 100):
    methods = ['Linear Probing', 'Quadratic Probing', 'Double Hashing']
    results = {}
    
    for method_name in methods:
        ht = HashTable(table_size)
        total_probes = 0
        successful_inserts = 0
        
        for key in dataset:
            if successful_inserts >= table_size:
                print(f"Warning: Table is full for {method_name}")
                break
            
            if method_name == 'Linear Probing':
                probes = ht.linear_probing(key)
            elif method_name == 'Quadratic Probing':
                probes = ht.quadratic_probing(key)
            else:  
                probes = ht.double_hashing(key)
            
            total_probes += probes
            successful_inserts += 1
        
        if successful_inserts > 0:
            avg_probes = total_probes / successful_inserts
        else:
            avg_probes = 0
        
        results[method_name] = {
            'average_probes': avg_probes,
            'successful_inserts': successful_inserts,
            'load_factor': successful_inserts / table_size
        }
    
    return results


def print_results(results: dict):
    print("\n" + "="*70)
    print("COMPARISON OF COLLISION RESOLUTION METHODS - OPEN ADDRESSING")
    print("="*70)
    print(f"{'Method':<20} {'Avg Probes':<15} {'Inserts':<10} {'Load Factor':<15}")
    print("-"*70)
    
    for method, data in results.items():
        print(f"{method:<20} {data['average_probes']:<15.4f} "
              f"{data['successful_inserts']:<10} {data['load_factor']:<15.4f}")
    
    print("="*70)



def main():
    DATASET_FILE = "string_dataset.txt"
    TABLE_SIZE = 1000  
    print("="*70)
    print("OPEN ADDRESSING COLLISION RESOLUTION METHODS")
    dataset = read_dataset(DATASET_FILE)
    
    if not dataset:
        print("No data to process. Exiting...")
        return
    
    results = compare_collision_methods(dataset, TABLE_SIZE)
    print_results(results)


if __name__ == "__main__":
    main()