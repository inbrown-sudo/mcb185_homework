# Saving throws against DCs of 5, 10, and 15

import random 

def roll_d20():
    return random.randint(1, 20)

def saving_throw(dc, mode='normal'): 
    if mode == 'normal': roll = roll_d20()
    elif mode == 'advantage': roll = max(roll_d20(), roll_d20())
    elif mode == 'disadvantage' : roll = min(roll_d20(), roll_d20())
    else: return None
    
    return roll >= dc

# Running simulation

def simulate(dc, mode, trials=100000):
    successes = 0
    for _ in range(trials):
        if saving_throw(dc, mode):
            successes += 1
    return successes / trials
    
dcs = [1, 2, 3]
modes = ['normal', 'advantage', 'disadvantage']

for dc in dcs:
    print(f'\nDC {dc}')
    for mode in modes:
        prob = simulate(dc, mode)
        print(f'{mode:13}: {prob:3f}')

