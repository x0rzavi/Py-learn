def unique(my_list):
    dupl = []
    uniq = []
    
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] in dupl:
                break
            if my_list[i] == my_list[j]:
                dupl.append(my_list[i])
                break
    
    for i in my_list:
        if i not in dupl:
            uniq.append(i)
    
    return uniq

my_list = input('Enter elements: ').split()
print('Unique elements:', unique(my_list))
