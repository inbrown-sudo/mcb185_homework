# Finding Pythagorean triples for triangles

def pythagorean_triples():
    for a in range(1, 99 ):
        for b in range(a, 99 ):   
            c = (a**2 + b**2 ) ** 0.5
            
            if c % 1 == 0: print(a, b, int(c))

pythagorean_triples()
