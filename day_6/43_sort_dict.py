my_dict = {"Eusebio": 120, "Cruyff": 104, "Pele": 150, "Ronaldo": 132, "Messi": 125}
sorted_list = sorted(my_dict.items(), key=lambda n: n[1])
sorted_dict = dict(sorted_list)
print(sorted_dict)
