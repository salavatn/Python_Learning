# list
# list.append(__object)
auto = [["Mitsubishi Outlander", "Mitsubishi Pajero Sport", "Mitsubishi ASX"]]
print("List of car:", auto)

auto.append(["Renault Arkana", "Renault Duster", "Renault Kaptur"])
print("List of car:", auto)

auto.append(["BMW X1","BMW X2", "BMW X3", "BMW X6"])
print("List of car:", auto)

# list.insert(__index, __object)
auto.insert(2,"MAZDA")
auto.insert(2,["Kia K5", "Kia K9"])
print("List of car:", auto)

# list.extend(__iterable)
carAudi = [["Audi A1","Audi A2","Audi A3","Audi A4"]]
auto.extend(carAudi)
print("List of car:", auto)


# =========================================
# list.sort()
guestList = [12,40,True,1,4,False,True]
numberList = [7,4,1,9,5,3,8,2,6]
nameList = ["b","f","s","u","e","d","h"]

guestList.sort()
nameList.sort()
#numberList.sort()
print(guestList,nameList,numberList)

# list.reverse()
guestList.reverse()
nameList.reverse()
numberList.reverse()
print(guestList,nameList,numberList)

# list.pop() - delete last element
print(numberList)
numberList.pop()
print(numberList)
numberList.pop(0)
print(numberList)

#list.remove()
# print(auto)
# auto.remove("MAZDA")
# print(auto)

#list.clear()
numberList.clear()
print("numberList.clear() \t",numberList)

#list.count()
print(auto.count("MAZDA"))

print(len(auto))