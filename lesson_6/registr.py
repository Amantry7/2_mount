import random

def regist():
    while True: 
        usernom = int(input("Введите свой номер: ")) 
        userage = int(input("Введите свой возраст: "))  
        if userage >= 18: 
            print("Продолжаем регистрацию ")
        else: 
            print("вам должно быть больше 18")
            break
        namlis = random.randint(10000,99999)
        print("на ваш номер прешол код")
        print("ваш код", namlis)
        usercode = int(input("Введите код: "))
        
        if usercode == namlis:
            print("код верный")
        else: 
            print("неверный код")
            break
        username = input("Введите имя пользевателя: ")
        userpass = (input("предумайте pin-code: "))
        password = (input("введите повторнно свой pin-code: ")) 
        if userpass != password: 
            print("pin-code не совподают") 
        elif len(password) != 4: 
            print("pin-code должно быть 4 цифры")   
        elif "123" in password: 
            print("Простой pin-code")   

        else: 
            print('pin-code сохранен')
            print("вы зарегистровались :)")
            break
regist()