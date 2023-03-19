
import numpy as np

total_cost = 0
total_income = 0

for game in range(100):
    cost = 0
    head = 0
    tail = 0
    while True:
        cost += 1
        total_cost += 1
        r = np.random.randint(0, 1)
        if r == 0:
            head += 1
        else:
            tail += 1
        dif = abs(head - tail)

        if dif >= 3:
            print(f"won 8 dollar cost  {cost} dollar")
            total_income += 8
            break
print(f"Total cost: {total_cost}, Total Income: {total_income}")
