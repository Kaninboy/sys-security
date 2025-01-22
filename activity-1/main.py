import hashlib
import itertools
import time

def hash_sha1(word):
    return hashlib.sha1(word.encode()).hexdigest()

def hash_md5(word):
    return hashlib.md5(word.encode()).hexdigest()

def apply_substitutions(word):
    substitutions = [
        ('o', '0'),
        ('l', '1'),
        ('i', '1'),
    ]
    variations = set([word])
    for old, new in substitutions:
        new_variations = set()
        for variation in variations:
            # Generate all possible positions for the substitution
            positions = [i for i, char in enumerate(variation) if char.lower() == old]
            for num_replacements in range(1, len(positions) + 1):
                for replacement_positions in itertools.combinations(positions, num_replacements):
                    new_variation = list(variation)
                    for pos in replacement_positions:
                        new_variation[pos] = new
                    new_variations.add(''.join(new_variation))
        variations.update(new_variations)
    
    # Generate all combinations of lower and uppercase letters
    all_variations = set()
    for variation in variations:
        combinations = map(''.join, itertools.product(*((c.lower(), c.upper()) for c in variation)))
        all_variations.update(combinations)

    return all_variations

# Question 1 - Find the original value of a hash
def find_original_value(hash_to_find, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for line in file:
            word = line.strip()
            variations = apply_substitutions(word)
            for variation in variations:
                if hash_sha1(variation) == hash_to_find:
                    print(f'Original value found: {variation}')
                    return variation
                if hash_md5(variation) == hash_to_find:
                    print(f'Original value found: {variation}')
                    return variation
    print('Original value not found')
    return None

# Question 2 - Create a rainbow table from a dictionary
def create_rainbow_table(dictionary_file, output_file):
    with open(dictionary_file, 'r') as file, open(output_file, 'w') as out_file:
        for line in file:
            word = line.strip()
            variations = apply_substitutions(word)
            for variation in variations:
                sha1_hash = hash_sha1(variation)
                out_file.write(f'{variation} {sha1_hash}\n')
    # print execution time
    print('Rainbow table created')

# Constants
DICTIONARY_FILE = '10k-most-common.txt'

# Question 1
TARGET_HASH = 'd54cc1fe76f5186380a0939d2fc1723c44e8a5f7'

# Question 2
RAINBOW_TABLE_FILE = 'rainbow_table.txt'

if __name__ == '__main__':
    # Question 1
    find_original_value(TARGET_HASH, DICTIONARY_FILE)

    # Question 2
    create_rainbow_table(DICTIONARY_FILE, RAINBOW_TABLE_FILE)

    # Question 3 - Execution time
    start_time = time.time()
    create_rainbow_table(DICTIONARY_FILE, RAINBOW_TABLE_FILE)
    print(f'Execution time: {time.time() - start_time} seconds')