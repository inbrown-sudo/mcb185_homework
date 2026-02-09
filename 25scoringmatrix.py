# Write a program that prints out a match-mismatch scoring matrix

import sys

alphabet = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

print(' ', end='')
for base in alphabet:
    print(f'{base:>3}', end='')
print()

for row_base in alphabet:
    print(f'{row_base}', end='')
    for col_base in alphabet:
        if row_base == col_base: print(f'{match:>3}', end='')
        else: print(f'{mismatch:>3}', end='')
    print()

# Command line = python3 25scoringmatrix.py ACGT +1 -1