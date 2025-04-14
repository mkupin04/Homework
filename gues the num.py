import random 

num = random.randint(1, 100)
gues = 0
attempt = random.randint(5, 15)

name = input(f"- Привіт! Як тебе звати? \n- ")
choice = input(f"\n- Приємно познайомитись, {name}! Хочеш зіграти в гру? (так або ні) \n- ")

while True:
    if choice == "так":
        print(f"\n- Я загадав число від 1 до 100 і ти маєш його відгадати: ")

        while True: 
            if gues == num:
                break
            
            elif attempt <= 0:
                break
            
            gues = int(input(f"- У тебе {attempt} спроб.\n- Я думаю це: "))

            if gues < num:
                print("\n- Твоє число менше загаданого\n")
                attempt -= 1

            elif gues > num:
                print("\n- Твоє число більше загаданого\n")
                attempt -= 1 
               
        if gues == num:
            print(f"- Вітаю! Ти вгадав моє число!\n")
            break

        elif attempt <= 0:
            print(f"- На жаль, ти програв. Моє число було: {num}")
            break
        
    elif choice == "ні":
        print("- Ну як хочеш. Бувай!")
        break

    else:
        print("- Я не зрозумів твою відповідь. Спробуй ще раз.")
        choice = input(f"- Хочеш зіграти в гру? (так або ні) \n- ")
