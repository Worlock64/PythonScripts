largest = 0
smallest = 0

while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    if num < largest :
        if smallest == 0:
            smallest = num
        elif num < smallest:
            smallest = num
    elif num > largest:
        largest = num
    
print("Maximum is ", largest)
print("Minimum is ", smallest)
    