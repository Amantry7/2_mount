import sqlite3
import random

connect = sqlite3.connect("cashier.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS cashier(
    id INTENGER PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    age INTEGER NOT NULL,
    works TEXT DEFAULT 'не работает',
    served INTEGER NOT NULL DEFAULT '0',
    revenue DOUBLE (8,2) NOT NULL DEFAULT '0,0');""")

class Work: 
    def __init__(self): 
        self.full_name = None
        self.age = None 
        self.works = None
        self.served = 0
        self.revenue = 0 
        
    def regist(self, full_name, age,  ):
        self.full_name = full_name
        self.age = age
        cursor.execute(f"""INSERT INTO cashier (full_name, age, works, served, revenue)
                       VALUES ('{full_name}', '{age}', 'не работает', 0, 0.0)""")   
        connect.commit()     
    def start_work(self, new_full_name): 
        self.full_name = new_full_name
        cursor.execute(f"UPDATE cashier SET works = 'работает' WHERE  full_name = '{new_full_name}'")
        connect.commit()        
        
    def finish(self,new_full_name, new_served, new_revenue): 
        self.full_name = new_full_name
        self.new_served = new_served
        self.new_revenue = new_revenue
        cursor.execute(f"UPDATE cashier SET works = 'не работает', served = '{self.new_served}', revenue = '{self.new_revenue}' WHERE full_name = '{new_full_name}'") 
        connect.commit()
        
        
    def main(self): 
        while True: 
            command = int(input("1-Регистрация 2-Начать смену 3-Закончить смену: ")) 
            if command == 1: 
                name = input("Введите свое имя: ")
                age = int(input("Введите свой возраст: "))
                print("вы успешно прошли регистрасию ")
                self.regist(name,age)
            elif command == 2:
                username = input("Введите свое имя: ")
                cho = int(input("Хотите начать смену 1-да 2-нет: "))
                if cho == 1:
                    self.start_work(username)
                    print(f"{self.full_name} вы начели свою смену") 
                else:
                    print("вы остались без зп")
            elif command ==3: 
                username = input("Введите свое имя: ")
                new_served = random.randint(1,200)
                new_revenue = random.randint(50000,100000)
                print(f"{self.full_name}  вы закончили смену")
                self.finish(username,new_served,new_revenue) 
                
magazin = Work() 
magazin.main()                        