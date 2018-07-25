import random

numbers_set = set()

while True:
    r_number = random.randint(0, 10000)
    if r_number in numbers_set:
        break
    numbers_set.add(r_number)
print(len(numbers_set)+1)
