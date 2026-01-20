# 10demo.py by Isabelle Brown

import math 

print('hello, again') #greeting
print(1.5e-2)
print(1 + 1)
print(2**3)
print(pow(2, 3))
print(2**0.5)
print(math.sqrt(2))
print(math.log(2))
#print(1 / 0)           # divide by zero error
#print(math.log(0))     # math domain error
#print(math.sqrt(-1))   # math domain error

print(0.1 * 1)
print(0.1 * 3)

a = 3                       # side of triangle
b = 4                       # side of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse 
print(c)

print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ', end='!\n')

def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c 
hyp = pythagoras(3, 4)
print(hyp)

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))

def pythagoras(a, b): return math.sqrt(a**2 + b**2)

def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h

def triangle_area(w, h): return rectangle_area(w, h) /2

s = 'hello world'
print(s, type(s))

a = 2
b = 2
if a == b:
	print('a equals b')
print(a, b)

def is_even(x):
	if x % 2 == 0: return True 
	return False 
	
print(is_even(2))
print(is_even(3))

c = a == b 
print(c)
print(type(c))

if a < b:
	print('a < b')
elif a > b:
	print('a > b')
else:
	print('a == b')

if   a < b: print('a < b')
elif a > b: print ('a > b')	
else:		print('a == b')

if a < b: print('a < b')
elif a <= b: print('a <= b')
elif a == b: print('this will never print!')

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if 	 a < b: print('a < b')
elif a > b: print('a > b')
else:		print('a == b')

print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

# a = 1
# s = 'G'
# if a < s: print('a < s')    This results in a Type error

def silly(m, x, b):
	y = m * x + b
print(silly(2, 3, 4))

def is_integer(x):			
	return x % 1 == 0
	
def is_probability(p):       
	return 0 <= p <= 1
	
def dna_molecular_weight(base):     
	base = base.upper()
	weight = {
	"A": 313.2, 
	"C": 289.2, 
	"G": 329.2, 
	"T": 304.2
	}
	return weight.get(base, None)
	
def dna_complement(base):            
	base = base.upper()
	complement = {
	"A": "T", 
	"T": "A", 
	"C": "G", 
	"G": "C"
	}
	return complement.get(base, None)     # Come back to these 4 
	
def max_of_three(a, b, c):
    return max(a, b, c)

def sensitivity(tp, fn):
    return tp / (tp + fn) if (tp + fn) != 0 else 0.0

def specificity(tn, fp):
    return tn / (tn + fp) if (tn + fp) != 0 else 0.0

def f1_score(tp, fp, fn):
    denom = 2 * tp + fp + fn
    return (2 * tp) / denom if denom != 0 else 0.0

    import math

def shannon_entropy(a, c, g, t):
    counts = [a, c, g, t]
    total = sum(counts)

    if total == 0:
        return 0.0

    entropy = 0.0
    for count in counts:
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)

    return entropy                           # Come back to these too
       




	
	
	
	
	
	
