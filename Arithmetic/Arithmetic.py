# 📊 Basic Arithmetic Operations with User Input

try:
    # Taking input from the user
    A = float(input("Enter the first number (A): "))
    B = float(input("Enter the second number (B): "))

    print("\n📈 Results of Arithmetic Operations:\n")

    print(f"➕ Addition (A + B): {A + B}")
    print(f"➖ Subtraction (A - B): {A - B}")
    print(f"✖️ Multiplication (A * B): {A * B}")
    
    if B != 0:
        print(f"➗ Division (A / B): {A / B}")
        print(f"🧮 Modulus (A % B): {A % B}")
        print(f"🔻 Floor Division (A // B): {A // B}")
    else:
        print("⚠️ Division, Modulus, and Floor Division not allowed (B = 0)")

    print(f"⚡ Exponentiation (A ** B): {A ** B}")

except ValueError:
    print("❌ Invalid input! Please enter numeric values.")
