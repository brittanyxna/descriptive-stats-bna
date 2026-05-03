# Print the introductory line
print("The new Carolina fight song:")

# Loop from 1 to 100
for i in range(1, 101):
    # Check if divisible by both 3 and 5 first (which is 15)
    if i % 3 == 0 and i % 5 == 0:
        print("TAR HEELS!")
    # Check if divisible by 3
    elif i % 3 == 0:
        print("TAR!")
    # Check if divisible by 5
    elif i % 5 == 0:
        print("HEELS!")
    # Otherwise, just print the number with an exclamation point
    else:
        print(f"{i}!")