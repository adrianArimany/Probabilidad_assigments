import itertools as it
from collections import Counter

x = it.product(range(0,10), repeat=4)
valid_numbers = [combo for combo in x if combo[0] != 0] 
# Exluide todo los tuples que inicial en 0, ya que se buscan solo los decimales, y un decimal no empieza con 0
ans = len(valid_numbers)
print(ans)

#9,000 números decimales de 4 dígitos

#B4

valid_numbers = [int("".join(map(str, perm))) for perm in it.permutations(range(10), 4) if perm[0] != 0 ]
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
    for perm in it.permutations(range(10), 4)  # Permutations of 4 digits
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
    for perm in it.permutations(range(10), 4)  # Permutations of 4 digits
    if perm[0] != 0  # First digit must not be zero
]
no_repeats = len(valid_numbers)

# Numbers with at least one repeated digit
with_repeats = total_numbers - no_repeats

# Output the results
print(f"Total numbers with no repeated digits: {no_repeats}")
print(f"Total numbers with one or more repeated digits: {with_repeats}")

x = it.product(range(0,10), repeat=4)
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
    digit_pairs = list(it.combinations(range(10), 2))
    
    count = 0
    numbers = []
    
    for pair in digit_pairs:
        # Create a list with each digit repeated twice
        digits = [pair[0], pair[0], pair[1], pair[1]]
        
        # Get all possible arrangements of these digits
        perms = set(it.permutations(digits))
        
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




S = it.product(range(10), repeat=4)
valid_numbers = [k for k in S if k[0] != 0]
digitsTwice = [r for r in valid_numbers if len(set(r)) == 2 and all(r.count(d) == 2 for d in set(r))]
print(len(digitsTwice))  # Output: 90

# More efficient version using sets and collections.Counter


S = it.product(range(10), repeat=4)
valid_numbers = (k for k in S if k[0] != 0) # Use a generator for efficiency
digitsTwice = [r for r in valid_numbers if len(set(r)) == 2 and all(count == 2 for count in Counter(r).values())]
print(len(digitsTwice)) # Output: 90

S = it.product(range(10), repeat=4)
valid_numbers = (k for k in S if k[0] != 0)
digitsTwice_count = sum(1 for r in valid_numbers if len(set(r)) == 2 and all(count == 2 for count in Counter(r).values()))
print(digitsTwice_count) # Output: 90