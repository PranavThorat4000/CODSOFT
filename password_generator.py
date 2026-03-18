# Password Generator Program

import random
import string

print("------ PASSWORD GENERATOR ------")

while True:
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Please enter a valid length")
            continue

        print("\nSelect password type:")
        print("1. Simple (only letters)")
        print("2. Medium (letters + numbers)")
        print("3. Strong (letters + numbers + symbols)")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            characters = string.ascii_letters
        elif choice == "2":
            characters = string.ascii_letters + string.digits
        elif choice == "3":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            print("Invalid choice")
            continue

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

    except:
        print("Invalid input! Please enter numbers only.")

    again = input("\nDo you want to generate another password? (yes/no): ")
    if again.lower() != "yes":
        print("Program closed.")
        break