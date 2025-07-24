# 🔢 Even or Odd Number Checker

try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"{num} is an Even number ✅")
    else:
        print(f"{num} is an Odd number 🔹")

except ValueError:
    print("❌ Invalid input. Please enter a valid integer.")
