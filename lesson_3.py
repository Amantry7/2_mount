class Computer: 
    def __init__(self, cpu, memory, make_computations): 
        self.__cpu = cpu
        self.__memory = memory
        self.__make_computations = make_computations        
    @property
    def cpu(self):
        return self.__cpu
    @property
    def memory(self):
        return self.__memory       
    @property
    def make_computations(self):
        add = self.__cpu + self.__memory 
        min = self.__cpu - self.__memory
        div = self.__cpu // self.__memory 
        mult = self.__cpu * self.__memory 
        print(f"результат cложение: {add}")
        print(f"результат вычитание: {min}")
        print(f"результат умножение: {mult}")
        print(f"результат деление: {div}")
        return self.__make_computations        
        

    
# comp = Computer(12, 2, "результат")
# comp.make_computations

class Phone: 
    __sim_card_list = ["+996500102907", "+996546765934","+996789432256"]

    def call(self,sim_card_nomer, call_to_nomer):
        self.sim_card_nomer = sim_card_nomer
        self.call_to_nomer = call_to_nomer
        if self.call_to_nomer == 1: 
            print(f"Идет звонок на номер +996500102907 (O!) ") 
        elif self.call_to_nomer == 2: 
            print(f"Идет звонок на номер +996546765934 (Megakg) ") 
        elif self.call_to_nomer == 3: 
            print(f"Идет звонок на номер +996789432256 (Beelanikg) ")

# cal = Phone()        
# cal.call("+996534353234", 1)

class SmartPhone(Computer,Phone): 
    def __init__(self, locution, distante, cpu, memory, make_computations):
        super().__init__(cpu, memory, make_computations)
        self.locution = locution 
        self.distante = distante 
    def loc(self): 
        print(f" маршрут построе с вашего место положение до {self.locution} - {self.distante} метров.") 

smart = SmartPhone("Globys", 654, 43,12,2)        
smart.make_computations
smart.loc()
smart.call("+996534353234", 3)
  

        
        