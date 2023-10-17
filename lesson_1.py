# # Ооп - объектное оринтировное програмирование: 

# class Car: 
#     model = "Mersedes-Bens"# aтребут класса
#     wheels = 4  
#     #__inet__ конструктор
      #     def __init__(self, model, year, color):
#         self.model = model 
#         self.year = year 
#         self.color = color  
        
#     def info(self): 
#         print(f"Бренд машины - {self.model}, Год выпуска - {self.year}, Цвет - {self.color}")

        
# Mersedes = Car("s-class", 2023, "white") 
# Bmw = Car("m5 f90", 2020, "black") 
# Mersedes.info() 
# Bmw.info()


# class Cow:
#     def make_sounde(self):   
#         print("Myy!")

# cow = Cow()        
# cow.make_sounde()
    
class Airplane: 
    def __init__(self,model, year, max_speed, capacity): 
        self.model = model 
        self.year = year 
        self.max_speed = max_speed 
        self.capacite = capacity 
        self.is_flying = False 
        self.odometer = 0
    def take_off(self): 
        self.is_flying = True 
        print(f"Самолет поднялся в воздух")
        
    def fly(self,distante):
        if self.is_flying: 
            self.odometer += distante 
            print(f"Cамолет пролител {distante} km") 
        else: 
            print("C начоло самолет должен взлететь ") 
        
    def land(self): 
        self.is_flying = False 
        print("Наш самолет удачно преземлился")
            
        
    def info_about_plane(self): 
        print(f"Модель - {self.model}") 
        print(f"Год выпуска - {self.year}") 
        print(f"Максемальная скорасть {self.max_speed} km\h") 
        print(f"Вмешаемость - {self.capacite} человек") 
        print(f"пройденая дистанция - {self.odometer} km") 
     
        
plane = Airplane('ah-4',1982, 1200,250)  
plane.take_off()
plane.fly(1000)
plane.fly(2222)
plane.land()
plane.info_about_plane()

# booing = Airplane("747", 2000, 2000,  2 )
# booing.take_off()
# booing.fly(2000)