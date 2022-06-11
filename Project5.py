auto = [["Mitsubishi Outlander", "Mitsubishi Pajero Sport", "Mitsubishi ASX"]]
auto.append(["Renault Arkana", "Renault Duster", "Renault Kaptur"])
auto.append(["BMW X1","BMW X2", "BMW X3", "BMW X6"])
auto.insert(0,"MAZDA")
auto.insert(2,["Kia K5", "Kia K9"])

carAudi = [["Audi A1","Audi A2","Audi A3","Audi A4"]]
auto.extend(carAudi)
print("List of car:", auto)

print("\n\n")

for X in auto:
    print("Elements of array = ",X)