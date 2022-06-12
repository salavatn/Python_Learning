# text = "Hello World!"
#
#
# print(text[6])          # Output is: W
# print(len(text))        # Output is: 12
# print(text.count("l"))  # Output is: 3
# print(text)             # Output is: Hello World!
# print(text.capitalize())# Output is: Hello world!
# print(text.upper())     # Output is: HELLO WORLD!
# print(text.lower())     # Output is: hello world!
# print(text.isupper())   # Output is: False
# print(text.islower())   # Output is: False
# print(text.lower())
#
#
# print("\n")
# textLower = "hello world again"
# print(textLower.islower())  # Output is: True
# print(textLower.isupper())  # Output is: False
#
# print("\n")
# print(text.find("o"))       # Output is: 4      Hell[o] World!  - index #4
# print(text.find("W"))       # Output is: 6      Hello [W]orld!  - index #6
# print(text.find("d"))       # Output is: 10     Hello Worl[d]!  - index #10
#

print("\n")
carList = "BMW, Audi, Mazda, Chevrolet, Nissan, Honda"
#print(carList.split(", "))
carArray = carList.split(", ")
print(carArray)         # Output is: ['BMW', 'Audi', 'Mazda', 'Chevrolet', 'Nissan', 'Honda']
print(carArray[3])      # Output is: Chevrolet

i = 0
for i in range(len(carArray)):
    carArray[i] = carArray[i].upper()
    i += 1
    print(carArray)
# print(carArray)

# Output:
# ['BMW', 'Audi', 'Mazda', 'Chevrolet', 'Nissan', 'Honda']
# ['BMW', 'AUDI', 'Mazda', 'Chevrolet', 'Nissan', 'Honda']
# ['BMW', 'AUDI', 'MAZDA', 'Chevrolet', 'Nissan', 'Honda']
# ['BMW', 'AUDI', 'MAZDA', 'CHEVROLET', 'Nissan', 'Honda']
# ['BMW', 'AUDI', 'MAZDA', 'CHEVROLET', 'NISSAN', 'Honda']
# ['BMW', 'AUDI', 'MAZDA', 'CHEVROLET', 'NISSAN', 'HONDA']