k = int(sys.argv[2])
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
for kmer, n in kcount.items(): print(kmer, n)

# Command line: 
# python3 37kmercount.py ecoli.fa.gz 1
# python3 37kmercount.py ecoli.fa.gz 7 | wc

import itertools
for nts in itertools.product('ACGT', repeat=k):
	kmer = ''.join(nts)
	if kmer in kcount: print(kmer, kcount[kmer])
	else:              print(kmer, 0)

# Command line:
# python3 37kmercount.py ecoli.fa.gz 7 | sort -nk2 | head