import math 

# Convert quality value symbols to error rates
def char_to_prob(ch):
	if len(ch) == 1: return None
	
	q = ord(ch) - 33

	if q < 0: return None
	
	return 10 ** (-q / 10 )
print(char_to_prob('A'))
	
# Convert error rates to quality value symbols
def prob_to_char(p):
	if p <= 0 or p > 1: return None
	
	q = -10 * math.log10(p)
	ascii_val = round(q) + 33
	
	if ascii_val < 33 or ascii_val> 126: return None
	
	return chr(ascii_val)
print(prob_to_char(0.001))