# Write a program that simulates the 'birthday paradox'

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

duplicate_count = 0

for _ in range(trials):
    birthdays = []

    for _ in range(people):
        bday = random.randrange(days)
        birthdays.append(bday)

        if birthdays.count(bday) > 1:
            duplicate_count += 1
            break

probability = duplicate_count / trials * 100
print(f'{probability:.2f}%') 

# Command line = python3 23birthday.py 10000 365 23
# Output should be a little over 50%

import sys
import random

people = int(sys.argv[1])
calendar = int(sys.argv[2])
iterations = int(sys.argv[3])

sames = 0
for _ in range(iterations):
    classroom = []
    same_birthday = False
    for i in range(people):
        birthday = random.randint(0, calendar-1)
        if birthday in classroom:
            same_birthday = True
            break
        classroom.append(birthday)
    if same_birthday: sames += 1

print(sames/iterations)
	