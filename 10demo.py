# 10demo.py by Isabelle Brown

import math 

print('hello, again')    #greeting 
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

def is_integer(n):		   # Determine if number is integer	
	return n % 1 == 0
print(is_integer(15))
	
def is_probability(p):     # Determine if valid probability    
	return 0 <= p <= 1
print(is_probability(15))
	
def dna_weight(letter):    # Determine dna weight   
	letter = ('G')
	if letter == 'A': return 313.2
	elif letter == 'T': return 304.2
	elif letter == 'C': return 289.2
	elif letter == 'G': return 329.2
	else: return None
print(dna_weight('G'))
	
def dna_complement(letter):           # Determine complement of DNA letter
	letter = ('G')
	if letter == 'A': return 'T'
	elif letter == 'T': return 'A'
	elif letter == 'C': return 'G'
	elif letter == 'G': return 'C'
	else: return None
print(dna_complement('G'))

def max_three(a, b, c ):			# Return maximum 3 numbers
	if a > b and a > c: return a
	elif b > a and b > c: return b
	else: return c
print(max_three(1, 2, 3 ))

def sensitivity(tp, fn):                       # sensitivity, true positive rate
	if (tp + fn) == 0: return None
	else: return tp / (tp + fn)
print(sensitivity(10, 50 ))

def specificity(tn, fp):					   # specificity, true negative rate
    if (tn + fp) == 0: return None
    else: return tn / (tn + fp)
print(specificity(10, 50 ))

def F1_score(tp, fp, fn):                      # Determine F1 score
    if 2 * tp + fp + fn == 0: return None
    else: return (2 * tp) / (2 * tp + fp + fn)
print(F1_score(10, 20, 30, ))

def shannon_entropy(a, c, g, t):               # Determine Shannon entropy
    total = a + c + g + t
    if total == 0: return 0.0

    entropy = 0.0
    for count in (a, c, g, t ):
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)

    return entropy  
print(shannon_entropy(1, 2, 3, 4 ))                         # Come back to these too
       




	
	
	
	
	
	
