# Same as 23 but make a list from the calendar 

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

duplicate_count = 0

for _ in range(trials):
    calendar = [0] * days
    shared = False

    for _ in range(people):
        birthday = random.randrange(days)
        calendar[birthday] += 1

        if calendar[birthday] > 1:
            shared = True
            break

    if shared: duplicate_count += 1

probability = duplicate_count / trials * 100
print(f'{probability:.2f}%')

# Command line = python3 24birthday.py 10000 365 23
# Not git pushed yet 
