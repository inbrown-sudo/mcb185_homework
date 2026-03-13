# The python version of this:
# gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -nr

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		if line.split():
			feature = f[2]
		if feature not in count: count[feature] = 0
		count[feature] += 1
for f, n in count.items(): print(f, n)

# Alternate of lines 6 and 7:
#if feature not in count: count[feature] = 1
#else:                    count[feature] += 1

# More compositions

count = {}
for nt in seq:
    if nt not in count: count[nt] = 0
    count[nt] += 1
    
# Sorting
# python3 36countgff.py ecoli.gff.gz | sort
# python3 36countgff.py ecoli.gff.gz | sort -n -k 2
# python3 36countgff.py ecoli.gff.gz | sort -nk2

# for k in sorted(count): print(k, count[k]) -> Sort inside python

# for k, v in sorted(count.items(), key=lambda item: item[1]):
#    print(k, v)
    
#d ef by_value(tuple):
#    return tuple[1]

# for k, v in sorted(count.items(), key=by_value):
#    print(k, v)