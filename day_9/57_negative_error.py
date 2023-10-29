try:
    n = float(input('Enter number: '))
    if n >= 0:
        print('Number is:', n)
    else:
        raise ValueError('Number is negative!')
except ValueError as err:
    print(err)
