# 🔍 Greatest of Three Numbers

try:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    c = int(input("Enter your third number: "))

    if a > b and a > c:
        print("✅ First number (a) is the greatest.")
    elif b > a and b > c:
        print("✅ Second number (b) is the greatest.")
    elif c > a and c > b:
        print("✅ Third number (c) is the greatest.")
    else:
        print("⚠️ Two or more numbers are equal and greatest.")

except ValueError:
    print("❌ Invalid input. Please enter valid integers.")
