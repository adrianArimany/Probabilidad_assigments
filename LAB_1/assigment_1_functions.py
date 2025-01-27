from itertools import permutations, combinations, product
from collections import Counter
from math import factorial
x = product(range(0,10), repeat=4)
valid_numbers = [combo for combo in x if combo[0] != 0] 
# Exluide todo los tuples que inicial en 0, ya que se buscan solo los decimales, y un decimal no empieza con 0
ans = len(valid_numbers)
print(ans)

#9,000 números decimales de 4 dígitos

#B4

valid_numbers = [int("".join(map(str, perm))) for perm in permutations(range(10), 4) if perm[0] != 0 ]
newAns = len(valid_numbers)
ansB = newAns - len(list(x))  
print(ansB)

#8,856 números con uno o más dígitos repetidos

# Total 4-digit numbers
total_numbers = 9 * 10 * 10 * 10  # 9000

# Numbers with no repeated digits
# Generate all 4-digit numbers where no digits repeat
valid_numbers = [
    int("".join(map(str, perm)))
    for perm in permutations(range(10), 4)  # Permutations of 4 digits
    if perm[0] != 0  # First digit must not be zero
]
no_repeats = len(valid_numbers)

# Numbers with at least one repeated digit
with_repeats = total_numbers - no_repeats

# Output the results
print(f"Total numbers with no repeated digits: {no_repeats}")
print(f"Total numbers with one or more repeated digits: {with_repeats}")


# Total 4-digit numbers
total_numbers = 9 * 10 * 10 * 10  # 9000

# Numbers with no repeated digits
valid_numbers = [
    perm
    for perm in permutations(range(10), 4)  # Permutations of 4 digits
    if perm[0] != 0  # First digit must not be zero
]
no_repeats = len(valid_numbers)

# Numbers with at least one repeated digit
with_repeats = total_numbers - no_repeats

# Output the results
print(f"Total numbers with no repeated digits: {no_repeats}")
print(f"Total numbers with one or more repeated digits: {with_repeats}")

x = product(range(0,10), repeat=4)
# Count numbers with all digits equal
repeated_digits = [
    int("".join(map(str, combo)))
    for combo in x  # Digits 1–9 repeated 4 times
    if len(set(combo)) == 1  # All digits must be the same
]

# Count the total
total_count = len(repeated_digits)

# Output the results
print(f"Total numbers with all 4 digits repeated: {total_count}")

def find_double_repeated_digits():
    # Get all possible pairs of digits (0-9) that could be our two repeated digits
    digit_pairs = list(combinations(range(0,10), 2))
    
    count = 0
    numbers = []
    
    for pair in digit_pairs:
        # Create a list with each digit repeated twice
        digits = [pair[0], pair[0], pair[1], pair[1]]
        
        # Get all possible arrangements of these digits
        perms = set(permutations(digits))
        
        # Filter out numbers that start with 0
        valid_perms = [p for p in perms if p[0] != 0]
        
        # Convert permutations to actual numbers and add to our list
        numbers.extend([int(''.join(map(str, p))) for p in valid_perms])
        count += len(valid_perms)
    
    return count, sorted(numbers)

# Run the function and display results
count, numbers = find_double_repeated_digits()
print(f"Total count: {count}")
print("Example numbers:", numbers[:10])




S = product(range(10), repeat=4)
valid_numbers = [k for k in S if k[0] != 0]
digitsTwice = [r for r in valid_numbers if len(set(r)) == 2 and all(r.count(d) == 2 for d in set(r))]
print(len(digitsTwice))  # Output: 90

# More efficient version using sets and collections.Counter


S = product(range(10), repeat=4)
valid_numbers = (k for k in S if k[0] != 0) # Use a generator for efficiency
digitsTwice = [r for r in valid_numbers if len(set(r)) == 2 and all(count == 2 for count in Counter(r).values())]
print(len(digitsTwice)) # Output: 90

S = product(range(10), repeat=4)
valid_numbers = (k for k in S if k[0] != 0)
digitsTwice_count = sum(1 for r in valid_numbers if len(set(r)) == 2 and all(count == 2 for count in Counter(r).values()))
print(digitsTwice_count) # Output: 90

#Problema A2

S = "SEERESS"

En = set(permutations(S))
resultA = len(En)

print(f"El conjunto de posibles palabras usando la palabra SEERESS es S = {resultA}")

#result 140
#Problema B2
ansB = sum(1 for k in En if k[0] == "S" and k[6] == "R")
print(f"La cantidad de palabras que empiezan en S y terminan en R es {ansB}")
#result 10
#Problema C2
count = 0
for z in range(5,8):
    sets = set(combinations(S, z))
    for x in sets:
        count += len(set(permutations(x)))
    
print(count)
#Result 530


word = "SEERESS"
total_unique_words = 0
letter_count = Counter(word)  # {'S': 2, 'E': 3, 'R': 1}

# Calculate for each possible length from 5 to full word length
for length in range(5, len(word) + 1):
    # Get all permutations of the given length
    perms = set()  # Using set to store unique permutations
    
    # Get all possible combinations of positions
    for perm in permutations(word, length):
        word_perm = ''.join(perm)
        perm_counter = Counter(word_perm)
        
        # Check if the count of each letter in permutation is less than or equal
        # to its count in the original word
        valid = True
        for letter in perm_counter:
            if perm_counter[letter] > letter_count[letter]:
                valid = False
                break
                
        if valid:
            perms.add(word_perm)
    
    print(f"Words of length {length}: {len(perms)}")
    total_unique_words += len(perms)

print(f"\nTotal number of possible words (5 or more letters): {total_unique_words}")


# Problema A2
S = "SEERESS"


# Problema C2
count = 0
for r in range(5, 8):  # Subset sizes: 5, 6, 7
    sets = combinations(S, r)  # Generate combinations of size r
    for x in sets:
        count += len(set(permutations(x)))  # Count unique permutations for each combination

print(f"La cantidad de palabras usando cinco o más letras es {count}")


# Helper function to calculate unique permutations for a subset
def unique_permutations_count(subset):
    # Count frequencies of each letter
    letter_counts = {}
    for letter in subset:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    
    # Calculate the denominator for repeated letters
    denominator = 1
    for count in letter_counts.values():
        denominator *= factorial(count)
    
    # Calculate unique permutations
    return factorial(len(subset)) // denominator

# Word and its letters
word = "SEERESS"

# Total count of unique permutations for subsets of 5, 6, and 7 letters
total_count = 0

# Loop through subset sizes: 5, 6, and 7
for r in range(5, 8):  # Subset sizes
    subsets = combinations(word, r)  # Generate combinations of size r
    for subset in subsets:
        total_count += unique_permutations_count(subset)  # Add unique permutations for each subset

print(f"La cantidad de palabras usando cinco o más letras es: {total_count}")



total_unique_words = 0
letter_count = Counter(S)

for length in range(1, len(S) + 1):
    perms = set()
    for perm in permutations(S, length):
        word_perm = ''.join(perm)
        perm_counter = Counter(word_perm)
        valid = True
        for letter in perm_counter:
            if perm_counter[letter] > letter_count[letter]:
                valid = False
                break
        if valid:
            perms.add(word_perm)
    if length >= 5:
        print(f"Words of length {length}: {len(perms)}")
        total_unique_words += len(perms)

print(f"\nTotal number of possible words (5 or more letters): {total_unique_words}")


# Helper function to calculate unique permutations
def unique_permutations_count(subset):
    letter_counts = {}
    for letter in subset:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    denominator = 1
    for count in letter_counts.values():
        denominator *= factorial(count)
    return factorial(len(subset)) // denominator

# Word
word = "SEERESS"

# Total count for subsets of size 5 and 6
total_count = 0

# Calculate unique permutations for sizes 5 and 6
for r in range(5, 7):  # Subset sizes 5 and 6
    subsets = combinations(word, r)
    for subset in subsets:
        total_count += unique_permutations_count(subset)

# Add result from statement a for size 7
total_count += 140  # Result from statement a

print(f"La cantidad de palabras usando cinco o más letras es: {total_count}")
