# TASK: https://stepik.org/lesson/3364/step/12?unit=947
teamA = int(input())
teamB = int(input())

count = 0
n = True

while n:
    count += teamA
    if (count / teamB % 1) == 0:
        print(count)
        n = False




# # TASK: https://stepik.org/lesson/3364/step/11?unit=947
# numbers = True
# sum = 0
#
# while numbers != 0:
#     numbers = int(input())
#     sum += numbers
#
# print(sum)


# https://stepik.org/lesson/3364/step/10?unit=947
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# sum = 0
#
# while a <= b:
#     sum += a
#     a += 1
# print(sum)


# https://stepik.org/lesson/3364/step/7?unit=947
# n = int(input())
# asterix = "*"
# i = 0
# while i < n:
#     print(asterix)
#     asterix += "  *"
#     i += 1
#
# c = 1
# n = int(input())
# while c <= n:
#     print("\t*" * c)
#     c += 1

# # https://stepik.org/lesson/3364/step/3?unit=947
# number = 5
#
# while number <= 55:
#     print(number, end=" ")
#     number += 2


# # https://stepik.org/lesson/5047/step/7?unit=1086
# ticket = str(input())
# #ticket = "090234"
# list = []
#
# for i in ticket:
#     list.extend(i)
#
# a = int(list[0]) + int(list[1]) + int(list[2])
# b = int(list[-1]) + int(list[-2]) + int(list[-3])
#
# if a ==b:
#     print("Счастливый")
# else:
#     print("Обычный")

