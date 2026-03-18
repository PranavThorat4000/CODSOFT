# Calculator Program

print("------ CALCULATOR ------")

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nSelect operation:")
        print("+  Addition")
        print("-  Subtraction")
        print("*  Multiplication")
        print("/  Division")

        op = input("Enter operation: ")

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero")
                continue
        else:
            print("Invalid operation")
            continue

        print("Result:", result)

    except:
        print("Invalid input! Please enter numbers only.")

    again = input("\nDo you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Calculator closed.")
        break