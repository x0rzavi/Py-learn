try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
except ValueError:
    print("Error: Enter valid numbers!")
except ZeroDivisionError:
    print("Error: Division by zero not possible!")
except KeyboardInterrupt:
    print("\nCtrl - C was pressed!")
