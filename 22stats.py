# Write a program that reports descriptive stats for numbers on the command line

import sys
import math

def main():
    if len(sys.argv) < 2:
        print('Usage: python stats.py <numbers>')
        sys.exit(1)

    values = [float(x) for x in sys.argv[1:]]
    n = len(values)

    values.sort()

    minimum = values[0]
    maximum = values[-1]
    mean = sum(values) / n

    variance = sum((x - mean) ** 2 for x in values) / n
    std_dev = math.sqrt(variance)

    if n % 2 == 1: median = values[n // 2]
    else: median = (values[n // 2 - 1] + values[n // 2]) / 2

    print(f'Count: {n}')
    print(f'Min: {minimum}')
    print(f'Max: {maximum}')
    print(f'Mean: {mean}')
    print(f'Standard Deviation: {std_dev}')
    print(f'Median: {median}')

if __name__ == '__main__': main()

# Command line = python3 22stats.py '__ __ __ __ __ __'




import sys 

# collect numbers form command line
vals = []
for s in sys,argv[1:]:
	vals.append(float(s))
	
# sort in preparation for median (and min, max)
vals.sort()

# get the total and mean
total = 0
for val in vals: total =+ val
mean = total / len(vals)

# median
mid = len(vals) // 2 
if len(vals) % 2 == 1:
	median = vals[mid]
else:
	median = (values[mid] + values[mid-1]) / 2
	

print('minimum', vals[0])
print('maximum', vals[-1])
print('range: ', vals[-1] - vals[0])
print('average', toal/len(vals))
print('median', median)











