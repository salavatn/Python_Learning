userLength = int(input("Enter length of array: "))
userArray = []
userCounter = 0

while userCounter < userLength:
    msg = "Enter element #" + str(userCounter + 1) + ": "
    userArray.append(input(msg))
    userCounter += 1

print("New array created: ",userArray)
