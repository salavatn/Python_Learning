##Lab-1
# from jinja2 import Template
# name = "Salavat"
# age = 28
#
# my_text = Template("Hello {{ set_name.upper() }}! Your age is {{ set_age/2+10 }}")
# msg = my_text.render(set_name=name, set_age=age)
#
# print(msg)


# # Lab-2
# from jinja2 import Template
# class Person:
#     def __init__(self, name, age):
#         self.get_name = name
#         self.get_age = age
#
# user = Person("Salavat", 29)
#
# text = Template("Hello everyone! I'm {{ set_user.get_name }} and {{ set_user.get_age }}.")
# msg = text.render(set_user = user)
#
# print(msg)


# # Lab-3
# from jinja2 import Template
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
#
# user = Person("Salavat", 29)
# myTemplate = Template("Hello, I'm {{ set_data.getName() }} and {{ set_data.getAge() }} years old! ")
# msg = myTemplate.render(set_data = user)
#
# print(msg)

