# First 10 numbers of the Fibonacci sequence 

def fibonacci_10():
    a = 0
    b = 1

    print(a)
    print(b)

    for _ in range(8):
        c = a + b
        print(c)
        a = b
        b = c
        
print(fibonacci_10())