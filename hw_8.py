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
    def start_work(self): 
        
        cursor.execute(f"UPDATE cashier SET works = 'работает' WHERE  full_name = '{self.full_name}'")
        connect.commit()        
        
    def finish(self, new_served, new_revenue): 
        self.new_served = new_served
        self.new_revenue = new_revenue
        cursor.execute(f"UPDATE cashier SET served = '{self.new_served}', revenue = '{self.new_revenue}' WHERE full_name = '{self.full_name}'") 
        connect.commit()
        
        
    def main(self): 
        while True: 
            command = int(input("1-Регистрация 2-Начать смену 3-Закончить смену: ")) 
            if command == 1: 
                name = input("Введите свое имя: ")
                age = int(input("Введите свой возраст: "))
                self.regist(name,age)
            elif command == 2:
                cho = int(input("Хотите начать смену 1-да 2-нет: "))
                if cho == 1:
                    self.start_work() 
                else:
                    print("вы остались без зп")
            elif command ==3: 
                new_served = random.randint(1,200)
                new_revenue = random.randint(50000,100000)
                self.finish(new_served,new_revenue) 
                
magazin = Work() 
magazin.main()                        