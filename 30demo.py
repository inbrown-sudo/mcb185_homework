# Files

fp = open(path)
for line in fp:
    do_something_with(line)
fp.close()

with open(path) as fp:
    for line in fp:
        do_something_with(line)
        
import gzip
with gzip.open(path, 'rt') as fp:
    for line in fp:
        print(line, end='')

     