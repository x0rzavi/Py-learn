import random


class BelowThresholdError(Exception):
    pass


try:
    while True:
        n = round(random.random(), 4)
        print(n)
        if n < 0.5:
            raise BelowThresholdError("Value below 0.5!")
except BelowThresholdError as err:
    print(err)
