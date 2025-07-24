# Student Grading System 📘

try:
    marks = float(input("Enter your marks (0 - 100): "))

    if marks < 0 or marks > 100:
        print("❌ Invalid input. Please enter marks between 0 and 100.")
    elif marks > 90:
        print("🎉 Excellent! Grade: A")
    elif marks > 75:
        print("👏 Well done! Grade: B")
    elif marks > 50:
        print("🙂 Good effort! Grade: C")
    elif marks > 35:
        print("😌 Needs improvement. Grade: D")
    else:
        print("💔 Sorry, you have failed.")

except ValueError:
    print("⚠️ Invalid input. Please enter a numeric value.")
