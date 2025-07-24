# 👋 Hello World Program

try:
    name = input("Enter your name: ")
    
    if name.strip() == "":
        print("⚠️ No name entered. Hello, World!")
    else:
        print(f"🌍 Hello, {name}! Welcome to Python.")

except Exception as e:
    print("❌ An unexpected error occurred:", e)
