# Write a program that reports descriptive stats for numbers on the command line

import sys
import math

def main():
    if len(sys.argv) < 2:
        print("Usage: python stats.py <numbers>")
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

    print(f"Count: {n}")
    print(f"Min: {minimum}")
    print(f"Max: {maximum}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Median: {median}")

if __name__ == "__main__": main()

# Command line = python3 22stats.py '__ __ __ __ __ __'