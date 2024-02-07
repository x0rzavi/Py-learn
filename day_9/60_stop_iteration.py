import random

c = 0
while True:
    print(int(random.random() * 10), end=" ")
    c += 1
    if c == 10:
        raise StopIteration("\nDisplayed 10 numbers!")
