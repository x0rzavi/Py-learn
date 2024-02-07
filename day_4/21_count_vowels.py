sentence = str(input("Enter sentence: "))
vowels = "aeiouAEIOU"
c = 0
for char in sentence:
    if char in vowels:
        c += 1
print("Number of vowels:", c)
