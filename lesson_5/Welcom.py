print("Привествую тебя мой дороогой игрок ")
print("Меня зовут Леонид Якубовичь и вы программе поле чудес!!!!!")
class Guest: 
    def __init__(self,name, age, city): 
        self.name = name 
        self.age = age 
        self.city = city
    def __str__(self): 
         return f"И нашего  сегодняшнего гостя зовут {self.name} и ему {self.age} приехол/a из {self.city}"
     
gue = Guest("Sema", 19, "Osh")
if __name__ == "__main__":
    print(gue)
    