# Death saves simulation, single

import random

def death_save():
    successes = 0
    failures = 0

    while True:
        roll = random.randint(1, 20)

        if roll == 1:
            failures += 2
        elif roll < 10:
            failures += 1
        elif roll < 20:
            successes += 1
        else:  # roll == 20
            return "revived"

        if failures >= 3:
            return "dead"
        if successes >= 3:
            return "stable"

# Repeating the simulation

def simulate_death_saves(trials=100000):
    results = {"dead": 0, "stable": 0, "revived": 0}

    for _ in range(trials):
        outcome = death_save()
        results[outcome] += 1

    for key in results:
        results[key] /= trials

    return results

# Probability results

results = simulate_death_saves()

print('Probability of death:     ', round(results['dead'], 3))
print('Probability of stabilize: ', round(results['stable'], 3))
print('Probability of revive:    ', round(results['revived'], 3))
