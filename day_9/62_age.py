class NegativeAgeError(Exception):
    pass

try:
    n = int(input('Enter age: '))
    if n < 0:
        raise NegativeAgeError('Error: Age cannot be negative!')
    print('Age is:', n)
except NegativeAgeError as err:
    print(err)
