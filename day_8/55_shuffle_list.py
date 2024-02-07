import random

n = int(input("Enter n: "))
ll = int(input("Enter lower limit: "))
ul = int(input("Enter upper limit: "))
numbers = [random.randint(ll, ul) for _ in range(n)]

print("Initial list:", numbers)
random.shuffle(numbers)
print("Final list:", numbers)
