dict1 = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}
dict2 = {'Ravi': 10, 'Rajnish': 9, 'Sanjeev': 15, 'Yash': 2, 'Suraj': 32}
dict = dict1.copy()

for key, value in dict2.items():
    dict[key] = value

print('Merged dictionary:', dict)
