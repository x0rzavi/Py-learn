import random
c = 0
try:
    while(True):
        print(int(random.random() * 10), end = ' ')
        c += 1
        if c == 10:
            raise StopIteration('\nDisplayed 10 numbers!')
except StopIteration as err:
    print(err)
