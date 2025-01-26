import itertools as it

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

