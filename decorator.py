# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# def myfunction():
#     return "Helloooo"

# @changecase
# def otherfunction():
#     return "I am Rubyyynaaa"

# print(myfunction())
# print(otherfunction())

# with aragument
# def changecase(func):
#     def myinner(x):
#         return func(x).upper()
#     return myinner

# @changecase
# def myfunction(nam):
#     return "Hello" + nam

# print(myfunction("Ruby"))

# Constructor
class student:
    def __init__(self, name, age, semester):
        self.name = name
        self.age = age
        self.semester = semester

s1 = student("Rubina", 19, 4)

print(s1.name)
print(s1.age)
print(s1.semester)