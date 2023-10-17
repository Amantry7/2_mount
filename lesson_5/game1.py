print("Так познакомились гостем теперь начнем игру") 
import random
words = ["apple", "spotify","youtube", "amazon","facebook","geeksstudeo"]
word = random.choice(words)
def game_start(): 

    word_letters = []
    attempts = 5 
    
    print("сегодня наш гость будет угодывать Лучшиие компание во всем мире ")
    print("На все пра все унего 5 попыток")
    print("пожелаем удачи")
    
    while attempts > 0: 
        hidden_word = ""
        for letter in word: 
            if letter in word_letters:
                hidden_word += letter
            else: 
                hidden_word +="_"
                  
                    
        print(f'наше загадоное слова {hidden_word}')
        print(f"осталось {attempts} попыток")
        user = input("Ввeдите букву: ").lower() 
    
        if user in word_letters: 
            print(f"Откроту букву {user}")
            continue 
        word_letters.append(user)
        if user not in word: 
            attempts -= 1
            print("ты не угодал :(") 
            
        if "_" not in hidden_word: 
            print("поздравляю вы выйграли")
            print(f"ваш приз это 300 акциий этой компаний {word}")
            break
        if attempts == 0: 
            print("вы проиграли ") 
            break
game_start()            
            
 