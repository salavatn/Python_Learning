# Learning https://youtu.be/vMD6-jzgDvI

# for NUMBER in range(5, 10, 2):
#     print(NUMBER)
#
# text = "Hello World"
# for X in text:
#     print(X)
#

# # Task 2
# count = 0
# text = "Hello World"
# print(text)
# mySearch = input("\nWhat symbol looking for: ")
#
# for X in text:
#     print("\n Searching \t", X, end="")
#     if X == mySearch:
#         count +=1
#         print("\t Count is",count, end="")
#

# # # Task 3
# i = 5
# while i < 15:
#     print(i)
#     i += 2
#
# print(i)

# # Task 4
# myCar =  True
# while myCar:
#     if input("My car is: ") == "Renault":
#         myCar = False
#     else:
#         print("Nope, try again. ", end="")


# Task 5
myNumber = int(input("Enter number: "))
myStep = int(input("Set step: "))
X = 0

for X in range(2, 100, myStep):
    print(X)
    if X == myNumber:
        break








