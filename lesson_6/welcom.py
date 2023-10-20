print("Привествую вас в Мбанк") 
while True: 
    choice = input("Хотите зарегистрироватся: ").lower()
    if choice == "да": 
        from registr import * 
        break
        
    elif choice == "нет": 
        break
    else: 
        print("ошибка вы должны зарегистроватся")    
        
