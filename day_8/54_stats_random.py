import random
import math
# import statistics

n = 10
numbers = [random.randint(1, n) for _ in range(10)]
numbers.sort()
sum1 = sum2 =  0
count = len(numbers)

mid = (n // 2) - 1 # index starts from 0
if n % 2 == 0:
    median = (numbers[mid] + numbers[mid + 1]) / 2
else:
    median = numbers[mid]

for n in numbers:
    sum1 += n
mean = sum1 / count

for n in numbers:
    sum2 += (n - mean) ** 2
var = sum2 / (n - 1)

print('Number list:', numbers)
print('Mean:', mean)
print('Median:', median)
print('Standard Deviation:', math.sqrt(var))

# print(statistics.mean(numbers))
# print(statistics.median(numbers))
# print(statistics.stdev(numbers))

