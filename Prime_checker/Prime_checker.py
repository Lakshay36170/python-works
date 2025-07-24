# 🔍 Prime Number Checker

try:
    num = int(input("Enter a number: "))

    if num <= 1:
        print("❗ Neither Prime Nor Composite")
    elif num == 2:
        print("✅ Prime Number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("❌ Composite Number")
                break
        else:
            print("✅ Prime Number")

except ValueError:
    print("⚠️ Invalid input. Please enter an integer.")
