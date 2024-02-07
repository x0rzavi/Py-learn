name = input("Enter employee names: ").split()
salary = input("Enter employee salaries: ").split()
salary = [float(n) for n in salary]
employee = {}

if len(name) != len(salary):
    print("Unequal number of entries")
    exit()

for i in range(len(name)):
    employee[name[i]] = salary[i]

print(employee)
