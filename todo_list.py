todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Завдання '{task}' додано до списку завдань.")

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Завдання '{task}' видалено зі списку завдань.")
    else:
        print(f"Завдання '{task}' не знайдено у списку завдань.")

def view_tasks():
    if todo_list:
        print("Список завдань:")
        for task in todo_list:
            print(f"- {task}")
    else:
        print("Список завдань порожній.")

def edit_task(old_task, new_task):
    if old_task in todo_list:
        index = todo_list.index(old_task)
        todo_list[index] = new_task
        print(f"Завдання '{old_task}' змінено на '{new_task}'.")
    else:
        print(f"Завдання '{old_task}' не знайдено у списку завдань.")

while True:
    print(f"\nДії для todo list:"
          "\n1. Додати завдання"
          "\n2. Видалити завдання"
          "\n3. Змінити завдання"
          "\n4. Переглянути завдання"
          "\n5. Вийти")
    choice = input("Оберіть дію: ")
                
    if choice == '1':
        add_task(input("Введіть завдання для додавання: "))

    elif choice == '2':
        if todo_list:   
            view_tasks()
            remove_task(input("Введіть завдання для видалення: "))
        else:
            print("Список завдань порожній.")
                
    elif choice == '3':
        if todo_list:
            view_tasks()
            old_task = input("Введіть завдання яке хочете змінити: ")
            new_task = input("Введіть нове завдання для заміни: ")
            edit_task(old_task, new_task)
        else:
            print("Список завдань порожній.")   
    
    elif choice == '4':
        view_tasks()
    
    elif choice == '5':
        print("Вихід з програми.")
        break
    else:   
        print("Неправильний вибір. Спробуйте ще раз.")
    
