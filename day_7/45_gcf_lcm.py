def hcf(a, b):
    if a == 0:
        return b
    else:
        return hcf(b % a, a)

def lcm(a, b):
    return (a * b) / hcf(a, b)

a = float(input('Enter a: '))
b = float(input('Enter b: '))
print('GCD: ', hcf(a, b))
print('LCM: ', lcm(a, b))
