# TASK: https://stepik.org/lesson/3366/step/7?unit=949

number_first = int(input())
number_last = int(input())

mylist = []

for i in range(number_first, number_last + 1):
    if i % 3 == 0:
        mylist.append(i)

n = len(mylist)
mySum = 0

for i in range(n):
    mySum += int(mylist[i])

# print(mylist)
# print("sum", mySum)
# print("n", n)
answer = mySum / n
print(answer)

# Lab 03 (easy): https://stepik.org/lesson/3366/step/5?unit=949
#
# a = int(input())
# b = int(input())
#
# s = 0
# if a % 2 == 0:
#     a += 1
#
# for i in range(a, b+1, 2):
#     s += i
#     print(s)

#
#
#
# # Lab 02 (hard): https://stepik.org/lesson/3366/step/3?unit=949
#
# y_first = int(input())
# y_last  = int(input())
# x_first = int(input())
# x_last  = int(input())
#
# def create_array_y():
#     arrya_y = []
#     for i in range(y_first, y_last + 1):
#         arrya_y.append(i)
#     return (arrya_y)
#
# def create_array_x():
#     array_x = []
#     for i in range(x_first, x_last + 1):
#         array_x.append(i)
#     return (array_x)
#
# x = create_array_x()
# y = create_array_y()
#
# number_of_element_x = len(x)
# number_of_element_y = len(y)
#
# # print("\t", end="")
# for i in range(number_of_element_x):
#     print("\t\t",x[i],sep="", end="")
#
# while len(y) != 0:
#     print("")
#     print(y[0], "\t\t", end="")
#     # print("Checking (number_of_element_x):",number_of_element_x)
#     for i in range(number_of_element_x):
#         multiplication = int(y[0] * x[i])
#         print(multiplication, "\t\t", end="")
#         # print("Checking Y1: ", y)
#         # x(i)
#     # print("")
#     y.pop(0)
#     # print("Checking Y2: ", y)
#
#
#
#
#
# # for i in range(x):
# #     print(i)
#
#
#
# # def multiplication_table():
# #     create_array_y()
#
#
# # for i in range(y_first, y_last):
# #     print(i, end="\t")
#
#
# # ## Lab 01
# # n = int(input())
# #
# # for i in range(n):
# #     for j in range(n):
# #         print("*  ", end="")
# #     print()
