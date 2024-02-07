p = float(input("Enter principal: "))
t = float(input("Enter time: "))
if p < 200000:
    r = 10
elif p >= 200000 and p <= 1000000:
    r = 12
else:
    r = 15
i = (p * r * t) / 100
print("Interest:", i)
