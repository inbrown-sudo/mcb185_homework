import argparse

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

# head --help
# Command line:
# python3 38dust.py e.coli.fa.gz 20 1.4

print('first', 'second')                       # positional only
print('first', 'second', sep='\t', end='\n')   # named
print('first', 'second', end='\n', sep='\t')   # named, different order

# Command line:
# python3 38dust.py
# python3 38dust.py e.coli.fa.gz
# python3 38dust.py e.coli.fa.gz --size 15 --entropy 1.2
# python3 38dust.py coli.fa.gz --lower

