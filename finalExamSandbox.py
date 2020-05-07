import random

for i in range(10):
    num = random.randint(10, 20)
    if num <= 15:
        continue
    print(num)
