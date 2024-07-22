# todo_list.py

tasks = []

def display_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task():
    display_tasks()
    task_number = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")

while True:
    print("\nTo-Do List:")
    display_tasks()
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        break
    else:
        print("Invalid choice, please choose again.")
