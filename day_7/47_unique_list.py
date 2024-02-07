def unique(my_list):
    dupl = []
    uniq = []

    for element in my_list:
        if element in uniq:
            dupl.append(element)
        else:
            uniq.append(element)

    uniq = [x for x in uniq if x not in dupl]
    return uniq


my_list = input("Enter elements: ").split()
print("Unique elements:", unique(my_list))
