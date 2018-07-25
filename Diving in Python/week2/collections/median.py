import random
import statistics
numbers = []
size = random.randint(10, 100)
for _ in range(size):
    numbers.append(random.randint(0, 100))

half_size = len(numbers)//2
median = None

numbers.sort()
print(numbers)

if size % 2 == 1:
    median = numbers[half_size]
else:
    median = sum(numbers[half_size-1:half_size+1])/2

print('Our median = {}'.format(median))
print('Standard median = {}'.format(statistics.median(numbers)))
