line1 = input("Enter string 1: ").lower()
line2 = input("Enter string 2: ").lower()

if sorted(line1) == sorted(line2):
    print("Anagrams")
else:
    print("Not Anagrams")
