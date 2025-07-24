# Loop with break
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)   # Only print if loop hasn't broken

# Loop with continue
for i in range(10):
    if i == 5:
        continue  # Skip printing when i is 5
    print(i)       # Print all other values

# Loop with pass
for i in range(5):
    if i == 2:
        pass        # Do nothing, just a placeholder
    print(i)        # Print every value including 2
