# # Lab learning https://www.youtube.com/watch?v=DZvNZ9l9NT4
#
# # # My examples
# # name = "Salavat"
# # age = 29
# # car = "Renault Arkana"
# #
# # print("Hello,",name,"!\n "
# # "I know - you drive on",car,"\n "
# # "and now",age,"years old.")
#
#
# # number = 10500
# # print("Result is:", number)
# # del number
# #
# # number = 10600
# # print("Result now:", number)
#
# number = 10500          # int
# digit = 4.5236          # float
# text = "Hello World!"   # string
# number_string = "5.2346"
# True_False = False      #bool
#
# print("number = ", number)
# print("digit = ", digit)
# print("text =", text)
#
# ## print(text + True_False)     # TypeError: can only concatenate str (not "bool") to str
# print(text + str(True_False))   # Hello World!False
#
# # print(digit + number_string)      # TypeError: unsupported operand type(s) for +: 'float' and 'str'
# print(str(digit) + number_string)   # 4.52365.2346
# print(digit + float(number_string)) # 9.7582


numX = float(input("Enter number X:"))
numY = float(input("Enter number Y:"))


print("Result of X + Y =", numX + numY)
print("Result of X * Y =", numX * numY)
print("Result of X - Y =", numX - numY)
print("Result of X / Y =", numX / numY)

numY += 10
print(numY)
numY *= 10
print(numY)
numY /=10
print(numY)
numY -=10
print(numY)
