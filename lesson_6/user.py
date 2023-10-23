class Curn:   
    def __init__(self,num_card): 
        self.__num_card = num_card
        self.balanse = 0
    # user_cho = int(input("1-папольнить баланс,2 - снять деньги " ))
    # if user_cho == 1:   
    def depozit(self): 
        amount = int(input("Введите сумму попалнение: "))
        self.balanse += amount
        print(f"вы успешно паполнели баланс на сумму: {amount} ")
        cho = input("хотите снять средства: ").lower()
        def __str__(self):
            return f"ваш баланс: {self.balanse}"
        if cho == "да": 
            self.repozit()
        else:
            pass
        
   
    
            
    # elif user_cho == 2:      
    def repozit(self):
            amount = int(input("Введите сумму знятие средств: "))
            if self.balanse <= amount: 
                print("не достаточно средств")
            else:   
                self.balanse -= amount
                print(f"вы успешно сняли средства: {amount}")
    def __str__(self):
        return f"ваш баланс: {self.balanse}"
    
    def choice(self):
        choice = int(input("Выберите 1 для поплнения или 2 для снятия: "))
        if choice == 1:
            self.depozit()
        elif choice == 2:
            self.repozit()
            
        
                
curn = Curn(543525)
curn.choice()
print(curn)
print(curn)