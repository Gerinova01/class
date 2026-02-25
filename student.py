class Student:
    name = ""
    age = 0
    height = 0
    gender = ""
    score = 0

    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender


    def learn(self, test):
        self.score += test

    def __str__(self):
        return (f'{self.name}, {self.age}, {self.height}, {self.gender}, {self.score}')
    
    def introduce(self):
        return f"Hello my name is {self.name}"

lajos = Student("Lajos", 13, 178, "Attack helicopter")
anna = Student("Anna", 15, 170, "B8-Bomber-plane")
print(lajos.height)
lajos.name = "Lajos"
lajos.age = 13
lajos.height = 178
lajos.gender = "Attack helicopter"
lajos.mood = "kiráj"
print(lajos.gender)
print(lajos.name)
print(lajos.score)
lajos.learn(10)
lajos.learn(10)
print(lajos.score)
print(lajos.mood)

print(lajos)
print(anna)