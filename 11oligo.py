def tm(a, c, g, t ): 
	length = a + c + g + t
	if length == 0: return None
	elif length <= 13: return (a + t ) * 2 + (g + c ) * 4       # If short oligo
	elif length > 12: return 64.9 + 41 * (g + c - 16.4 ) / length
print(tm(1, 2, 3, 4 ))
	