class Student:
    name = ""
    age = 0
    height = 0
    gender = ""
    score = 0

    def learn(self, test):
        self.score += test

    def __str__(self):
        return (f'{self.name}, {self.age}, {self.height}, {self.gender}, {self.score}')

lajos = Student()
anna = Student()
print(lajos.height)
lajos.name = "Lajos"
lajos.age = 13
lajos.height = 178
lajos.gender = "Attack helicopter"
print(lajos.gender)
print(lajos.name)
print(lajos.score)
print(lajos.learn(10))
print(lajos.score)

print(lajos)
print(anna)