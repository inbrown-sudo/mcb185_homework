# Strings 

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

import math 

print('{} {:.3f}'.format('str.format', math.pi))

print('%s %.3f' % ('printf', math.pi))

# Indexes 

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
	print(nt, end=' ')
print()

for i in range(len(seq)):
	print(i, seq[i])

# Slices

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5])			   # both ABCDE
print(s[5:len(s)], s[5:1]) 	       # both FGHIJ
print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)

# Tuples

tax = ('Homo', 'sapiens', 9606)		# construct tuple
print(tax)	
# s[0] = 'C'        				-> returns error
# tax[0] = 'human'  				-> returns error
print(tax[0])						# index
print(tax[::-1])					# slice					

# enumerate() 

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)

# zip()

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
for nt, name in zip(nts, names):
	print(nt, name)
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

# Lists

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# list()

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

# split() and join()

text = 'good day to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

# Searching

if 'A' in alph: print('yay')
if 'a' in alph: print ('no')

print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z'))	-> returns error
print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# Write a function that returns the minimum value of a list

def minimum(val):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
	
# Write a function that returns both the minimum and maximum values of a list

def min_max(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	
# Write a function that returns the mean of the values in a list

def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
	
# Write a function that computes the entropy of a probability distribution

import math 

def entropy(prob):
	h = 0
	for p in prob:
		h -= p * math.log2(p)
	return h 
print(entropy([0.2, 0.3, 0.5]))
	
# Write a function that computes the Kullback-Leibler distance between two sets of probability distributions 

import math 

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
		return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(dkl(p1, p2))
	
# input()

# line = input('type something and hit return: ')
# print('that line was', len(line), 'characteres long')

# sys.argv

import sys
print(sys.argv)

# Converting Types

i = int('42')
x = float('0.61803')
print(i * x)

# x = float('hello')










