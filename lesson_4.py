# class Computer:
#     def __init__(self, cpu, memory):  # Исправлено: это должен быть метод init, а не init
#         self.__cpu = cpu
#         self.__memory = memory

#     @property
#     def cpu(self):
#         return self.__cpu

#     @property
#     def memory(self):
#         return self.__memory

#     def __add__(self, other): 
#         if isinstance(other, Computer):
#             return Computer(self.cpu + other.cpu, self.memory)
#     def __sub__(self, other): 
#         if isinstance(other, Computer):
#             return Computer(self.cpu - other.cpu, self.memory)
#     def __mul__(self, other): 
#         if isinstance(other, Computer):
#             return Computer(self.cpu * other.cpu, self.memory)
        
#     def __floordiv__(self, other): 
#         if isinstance(other, Computer):
#             return Computer(self.cpu // other.cpu, self.memory)
#         else:
#             return None
    

#     def __str__(self):
#         return f"Computer with CPU: {self.cpu}, Memory: {self.memory}"

# comp1 = Computer(12, 12)
# comp2 = Computer(13, 12)


# print(comp1 + comp2)
# print(comp1 - comp2)
# print(comp1 * comp2) 
# print(comp1 // comp2)


# class Phone: 
#     def __init__(self,sim_cards_list): 
#         self.__sim_cards_list = sim_cards_list
#     @property
#     def sim_cards_list(self): 
#         return self.__sim_cards_list
#     @sim_cards_list.setter
#     def sim_cards_list(self,sim_list): 
#         self.sim_cards_list = sim_list
#     def __call__(self,sim_card_number, call_to_number):
#         self.sim_card_number = sim_card_number 
#         self.call_to_number = call_to_number
#     def __str__(self): 
#         if self.sim_card_number == 1: 
#             return f"Идет звонок на номер {self.call_to_number}, {self.sim_card_number} (O!) "
#         elif self.sim_card_number == 2: 
#             return f"Идет звонок на номер {self.call_to_number}, {self.sim_card_number} (Megakg) "
#         elif self.sim_card_number == 3: 
#              return f"Идет звонок на номер {self.call_to_number}, {self.sim_card_number} (Beelankg) "
# phon = Phone(["O!,", "Mega", "Beelankg"])
# phon(2, +996543352432)
# print(phon)
        
        
# class Smartphone(Computer, Phone): 
#     def __init__(self, locution, distante, cpu, memory, ):
#         super().__init__(cpu, memory, )
#         self.locution = locution
#         self.distante = distante 
#     def __str__(self):
#         return f"маршрут построен с вашего место положение до {self.locution} - {self.distante} метров" 
    
# loc = Smartphone("Globys", 34242, 12,32)
# print(loc)
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
print(gue)
