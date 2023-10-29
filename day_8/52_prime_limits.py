from prime import prime

ll = int(input('Enter lower limit: '))
ul = int(input('Enter upper limit: '))
for i in range(ll, ul + 1):
    if prime(i):
        print(i, end = ' ')
