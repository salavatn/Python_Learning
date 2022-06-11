
# print(value, sep, end, file, flush)

print("Hello", 435, 4.3, "Hi again")
print("Hello", 435, 4.3, "Hi again", sep="")
print("Hello", 435, 4.3, "Hi again", sep=" |||| ")

# using end="\n"
print(end="\n")
print("Dear Colleagues!", "Today we are scheduled a meeting \n")
print("Dear Colleagues!",end="")
print("Today we are scheduled a meeting")

# using escaping characters \* or \"text\"
print(end="\n")
print("Your file available here: \\\\fileserver\\docs\\ \n")

# using \n option (Next Line)
print(" My first strin \n Second String \n Third String \n")

# using \t option (Tabulation)
print("\t I'm using Tab here")



# x * y =
print("Result of (5 * 5) =", 5 * 5, "\n")

# x ** y =
print("Result of (5 ** 2) =", 5 ** 2)
print("Result of (2 ** 9) =", 2 ** 9)
print("Result of (5 ** 3) =", 5 ** 3)
print("Result of (5 ** 4) =", 5 ** 4)
print("Result of (2 ** 10) =", 2 ** 10)
print("Result of (2 ** 8) =", 2 ** 8)


# x / y =
print("Result of (5 / 1) =", 5 / 1)
print("Result of (5 / 2) =", 5 / 2)
print("Result of (5 / 3) =", 5 / 3)
print("Result of (5 / 4) =", 5 / 4,  "\n")

# x // y =
print("Result of (5 // 1) =", 5 // 1)
print("Result of (5 // 2) =", 5 // 2)
print("Result of (5 // 3) =", 5 // 3)
print("Result of (5 // 4) =", 5 // 4)

# round(x / y)
print("Result of (6/10) =", 6 / 10)
print("Result of round(6/10) =", round(6/10))
print("Result of (5/10) =", 5/10)
print("Result of round(5/10) =", round(5/10))
print("Result of (4/10) =", 4/10)
print("Result of round(4/10) =", round(4/10))
print("Result of (3/10) =", 3/10)
print("Result of round(3/10) =", round(3/10))


# min(5,77,0,-2), max(5,77,0,-2), abs(-5,-77), pow(2,10), round(5/3)
print("min(5,77,0,-2) \t =", min(5,77,0,-2))
print("max(5,77,0,-2) \t =", max(5,77,0,-2))
print("abs(-77) \t\t =", abs(-77))
print("pow(2,10) \t \t =", pow(2,10))
print("round(5/3) \t\t =", round(5/3))

# input()
input("Enter name:")
input("Enter your age:")
input("Enter your number:")

