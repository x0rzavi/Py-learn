try:
    while True:
        n = float(input("Enter number: "))
        print("Square:", n**2)
except ValueError:
    print("Error: Enter valid values!")
except KeyboardInterrupt:
    print("\nCtrl - C was pressed!")
