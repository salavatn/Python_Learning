# Lesson 4: https://youtu.be/SUDNfS_0X-Q

# number = float(input("Guess the number: "))
#
# if number == 23:
#     print("Correct!")
#
# if number > 23:
#     print("Check again, need min")
#
# if number < 23:
#     print("Check again, need max")
#
#
# vacation = False
#
# if vacation:
#     print("Let's go to party")
# else:
#     print("Go to work")

#
# myNum = float(input("Set the number:"))
#
# if myNum >= 10:
#     print("Your number is bigger then 10")
# elif myNum <= 0:
#     print("Your number is less then 0")
# else:
#     print("Your number around 1 - 9")

# What city are you from?
# print("What city are you from? Please, select from bellow list \n"
#       "● Moscow \n"
#       "● Saint-Petersburg \n"
#       "● Kazan \n"
#       "● Ufa \n")
#
userCity = input("Enter your location:")

if userCity == "Moscow" or userCity == "Saint-Petersburg":
    print("Здравствуйте, стоимость ваших услуг 500 рублей")
elif userCity == "Kazan":
    print ("Исәнмесез,өчпочмакны телисезме?")
elif userCity == "Ufa":
    print("Сәләм барыһына ла!")
else:
    print("Бар hыпырт мынан")


# # Условный (тернарный) оператор
# data = int(input("How old are you?"))
# age = "twenty nine" if data == 29 else "what?"
# print(age)