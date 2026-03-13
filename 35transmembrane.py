import sys
fasta = sys.argv[1]

kd = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def read_fasta(filename):
    name = None
    seq = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if line.startswith('>'):
                if name:
                    yield name, ''.join(seq)
                name = line[1:]
                seq = []
            else: seq.append(line)
        if name:
            yield name, ''.join(seq)

def avg_kd(seq):
    return sum(kd[a] for a in seq) / len(seq)
    
for name, seq in read_fasta(fasta):
    signal = False
    tm = False

    for i in range(0, min(30-8+1, len(seq)-7)):
        win = seq[i:i+8]
        if 'P' in win: continue
        if avg_kd(win) >= 2.5:
            signal = True
            break

    for i in range(30, len(seq)-10):
        win = seq[i:i+11]
        if 'P' in win: continue
        if avg_kd(win) >= 2.0:
            tm = True
            break

    if signal and tm: print(name)