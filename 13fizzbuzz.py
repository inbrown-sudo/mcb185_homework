for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0: print(i, 'fizzbuzz', end=' ')
	elif i % 5 == 0: print(i, 'buzz', end=' ')
	elif i % 3 == 0: print(i, 'fizz', end=' ')
