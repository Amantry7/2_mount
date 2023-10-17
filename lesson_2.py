class Person:
    def __init__(self, fullname, age, is_married): 
        self.fullname = fullname 
        self.age = age 
        self.is_married = is_married
                 
    def introduce_myself(self):
        print(f"Меня зовут {self.fullname}, и мне {self.age} лет, и я {self.is_married}.")
        
# per = Person("Aman", 23, "не женат")
# per.introduce_myself() 

class Student(Person): 
    def __init__(self, fullname, age, is_married):
        Person.__init__(self, fullname, age, is_married)
        
    def average_value(self,):  
        points = {"алгебра": 5, "физика": 4, "химия": 4 } 
        for i,af in points.items():
            balls = points.values() 
            a = sum(balls) / len(balls)
        print(f"средний балл {a}")
    
        
stu = Student("Aman", 15, "не женат") 
stu.introduce_myself()
stu.average_value()
        
    
    
class Teacher(Person): 
    def __init__(self, fullname, age, is_married, salary, experience):
         Person.__init__(self, fullname, age, is_married) 
         self.salary = salary
         self.experience = experience 
         
    def bonus(self): 
        for i in range(self.experience): 
            self.salary += 3000
        print(f"Ваша зарплата стала: {self.salary} ")
         
teach = Teacher("Галина Василевна", 43, "жената", 25000, 3)
teach.introduce_myself()
teach.bonus()
    
        


        