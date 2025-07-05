
import random
import matplotlib.pyplot as plt

# Define moves and what beats what
moves = ['rock', 'paper', 'scissors']
beats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

# Game logic
def get_result(a, b):
    if a == b:
        return 'Draw'
    elif beats[a] == b:
        return 'A wins'
    else:
        return 'B wins'

def case1():
    return random.choices(moves, weights=[0.5, 0.25, 0.25])[0]

# case 1 simulation
results = {'A wins': 0, 'B wins': 0, 'Draw': 0}
rounds = 10000

for _ in range(rounds):
    a = random.choice(moves)
    b = case1()
    outcome = get_result(a, b)
    results[outcome] += 1

# case 1 results
print("Case 1 Results:", results)
plt.bar(results.keys(), results.values(), color=['orange', 'red', 'yellow'])
plt.title("Player A vs Player B")
plt.ylabel("Count")
plt.show()

# Counter dictionary
counter_move = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

def case2(prev_a):
    if prev_a is None:
        return random.choice(moves)
    return counter_move[prev_a]

# case 2 simulation
results = {'A wins': 0, 'B wins': 0, 'Draw': 0}
rounds = 10000
prev_a = None

for _ in range(rounds):
    a = random.choice(moves)
    b = case2(prev_a)
    prev_a = a
    outcome = get_result(a, b)
    results[outcome] += 1

# case 2 results
print("Case 2 Results:", results)
plt.bar(results.keys(), results.values(), color=['orange', 'red', 'yellow'])
plt.title("Player A vs  Player B")
plt.ylabel("Count")
plt.show()

#case 3 simulation
results = {'A wins': 0, 'B wins': 0, 'Draw': 0}
rounds = 10000

for _ in range(rounds):
    a = case1()
    b = case2(prev_a)
    outcome = get_result(a, b)
    results[outcome] += 1

# case 3 results
print("Case 3 Results:", results)
plt.bar(results.keys(), results.values(), color=['orange', 'red', 'yellow'])
plt.title("Player A vs  Player B")
plt.ylabel("Count")
plt.show()
