daily_tasks = {}

while True:
    user_choice = input("\n   Планування щоденних задач\n"
                        "1. Додати задачу\n"
                        "2. Відмітити виконану задачу\n"
                        "3. Видалити задачу\n"
                        "4. Переглянути список задач\n"
                        "5. Вихід\n"
                        "Введіть дію для щодених задач: ")

    if user_choice == "1":
        task = input("Введіть задачу: ")
        daily_tasks[task] = "{task} | не виконано"
        print(f"Задачу додано.")
    
    elif user_choice == "2":
        print(f"Список задач", daily_tasks)
        task = input("Введіть задачу яку виконано: ")
        if task in daily_tasks:
            print(f"Задача '{task}' виконана.")
            daily_tasks[task] = "{task} | виконано"
        else:
            print(f"Задачу не знайдено.")   

    elif user_choice == "3":
        if task in daily_tasks:
            del daily_tasks[task]
            print(f"Задачу '{task}' видалено.")
        else:
            print(f"Задачу '{task}' не знайдено.")
    
    elif user_choice == "4":
        if daily_tasks:
            print("\n Всі задачі: ")
            for task in daily_tasks.items():
                print(f"{task}")
        else:
            print(f"Список задач порожній!")   

    elif user_choice == "5":
        print("Вихід")
        break
    
    else:
        print("Неправильний вибір! Спробуйте ще раз.")

