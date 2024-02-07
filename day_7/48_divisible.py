is_divisible = lambda n: n % 5 == 0 and n % 7 == 0
ll = int(input("Enter lower limit: "))
ul = int(input("Enter upper limit: "))
num_list = []

for i in range(ll, ul + 1):
    if is_divisible(i):
        num_list.append(i)

print("Numbers divisible:", num_list)
