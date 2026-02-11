def ascii_sum_hash(s, M=1000000):
    total = sum(ord(ch) for ch in s)
    return total % M

def polynomial_rolling_hash(s, p=31, M=1000000):
    hash_value = 0
    power_of_p = 1
    for ch in s:
        hash_value = (hash_value + (ord(ch) * power_of_p)) % M
        power_of_p = (power_of_p * p) % M
    return hash_value

def count_collisions(strings, hash_function, M=1000000):
    hash_table = {}
    collisions = 0
    for s in strings:
        h = hash_function(s, M)
        if h in hash_table:
            collisions += 1
            hash_table[h].append(s)
        else:
            hash_table[h] = [s]
    return collisions, hash_table

def main():
    filename = "string_dataset.txt"
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            unique_strings = [line.strip() for line in f if line.strip() != ""]
    except FileNotFoundError:
        print(f"file '{filename}' not found.")
        return

    if not unique_strings:
        print("datset is empty .")
        return

    print(f"numbers of uniqe string: {len(unique_strings)}")

    M = 1000  
    collisions_ascii, table_ascii = count_collisions(unique_strings, ascii_sum_hash, M)
    collisions_poly, table_poly = count_collisions(unique_strings, polynomial_rolling_hash, M)
    print("\n--- result ---")
    print(f"1. ASCII (with M={M}):")
    print(f"numbers  of colision: {collisions_ascii}")
    print(f"index that insert: {len(table_ascii)}")
    print(f"\n2. Polynomial Rolling Hash (basis 31, M={M}):")
    print(f"number colision: {collisions_poly}")
    print(f"index that insert: {len(table_poly)}")


if __name__ == "__main__":
    main()