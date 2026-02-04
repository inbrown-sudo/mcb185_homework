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
# s[0] = 'C'        				-> generates error
# tax[0] = 'human'  				-> generates error
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










